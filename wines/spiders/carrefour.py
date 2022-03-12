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
"""

class CarrefourClickSpider(scrapy.Spider):
    name = 'carrefour'
    allowed_domains = ['carrefour.es']
    start_urls = ['https://www.carrefour.es/bodega/vinos-tintos/vinos-tintos-nacionales/ver-todos/N-1dxafdm/c', 'https://www.carrefour.es/bodega/vinos-blancos/vinos-blancos-nacionales/ver-todos/N-distyh/c', 'https://www.carrefour.es/bodega/vinos-rosados/vinos-rosados-nacionales/ver-todos/N-1yz8sfs/c']

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
