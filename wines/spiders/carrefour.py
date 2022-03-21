import scrapy
import time
import re

"""
Command to scrape --> scrapy crawl carrefour -o carrefour.csv
Fortunately Carrefour's web is not provided with anticrawler blocking for Scrapy: https://www.carrefour.es/robots.txt
There are 45 pages in total for each url.
=====KNOWLEDGE=====
name = firstWine.css("a.js-gap-product-click::text").get().replace("\n", "")
price = firstWine.xpath("//p[contains(@class,'price price-oferta')]/text()").extract()[0].replace("\n", "")
winery = firstWine.css('a::attr(title)').re(r"^Buscar\sproductos\spor\sla\smarca\s*(.*)")[0]
location = firstWine.css('a::attr(title)').re(r"^D.O.\s*(.*)")[0].replace("Ca. ", "")
# https://blog.appliedinformaticsinc.com/manipulate-scrapy-start_urls-before-a-request-is-made/
# https://stackoverflow.com/questions/9322219/how-to-generate-the-start-urls-dynamically-in-crawling
"""

class CarrefourClickSpider(scrapy.Spider):
    name = 'carrefour'
    allowed_domains = ['carrefour.es']

    red_urls = [
        f'https://www.carrefour.es/bodega/vinos-tintos/vinos-tintos-nacionales/ver-todos/N-1dxafdm/c?No={n}&Nr%3DAND%28product.salepointWithActivePrice_004583%3A1%2Cproduct.shopCodes%3A004583%2COR%28product.siteId%3AbodegaSite%29%29OR%29'
        for n in range(0, 1028, 24)]
    white_urls = [
        f'https://www.carrefour.es/bodega/vinos-blancos/vinos-blancos-nacionales/ver-todos/N-distyh/c?No={n}&Nr%3DAND%28product.salepointWithActivePrice_004583%3A1%2Cproduct.shopCodes%3A004583%2COR%28product.siteId%3AbodegaSite%29%29OR%29'
        for n in range(0, 429, 24)]
    rose_urls = [
        f'https://www.carrefour.es/bodega/vinos-rosados/vinos-rosados-nacionales/ver-todos/N-1yz8sfs/c?No={n}&Nr%3DAND%28product.salepointWithActivePrice_004583%3A1%2Cproduct.shopCodes%3A004583%2COR%28product.siteId%3AbodegaSite%29%29OR%29'
        for n in range(0, 80, 24)]
    start_urls = red_urls + white_urls + rose_urls

    def parse(self, response):
        for link in response.css('a.js-gap-product-click::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)

    def parse_categories(self, response):
        container_color = response.css("div.column-desc-items")
        wine_table = response.css("div.item-inner.item-table")
        dataList = wine_table.css("td.w50")
        yield {
            'winery': response.css('p.name-marca.lora a::text').get(),
            'location': response.css('p.name-formato.lora a::text').get(),
            'country': 'Spain',
            'name': response.css('h1.tileDetailBodega.title-03.apercu::text').get(),
            'color': container_color.css("p::text")[0].get(),
            'variety': None,
            'price': response.css('span.js-price-total::text').get(),
            'rating': None,
            'body': None,
            'acidity': self.get_acidity(dataList),
            'crawler_day': time.strftime("%Y-%m-%d"),
            'alcohol_percentage': self.get_alcohol_percentage(dataList),
            'editors_choice': None,
            'id': None,
            'wine_review_link': None,
            'wine_review_publish_date': None,
            'source': "carrefour"
        }

    def get_acidity(self, dataList):
        if(re.match(re.compile("\nAcidez\stotal"), dataList.css("p::text")[4].get())):
            return dataList.css("p::text")[5].get()
        else:
            return None

    def get_alcohol_percentage(self, dataList):
        if(re.match(re.compile("^Graduación\salcohólica"), dataList.css("p::text")[0].get())):
            return dataList.css("p::text")[1].get()
        else:
            return None
