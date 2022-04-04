from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
#import time
#import re

"""
Command to scrape --> scrapy crawl carrefour -o carrefour.csv
Fortunately Carrefour's web is not provided with anticrawler blocking for Scrapy: https://www.carrefour.es/robots.txt
There are 45 pages in total for each url.
"""

class WineItems(Item):
    winery = Field()
    name = Field()
    origin = Field()
    price = Field()
    price_final = Field()
    color = Field()
    aging = Field()
    year = Field()
    description = Field()
    parker_score = Field()
    testing_view = Field()
    testing_nose = Field()
    testing_mouth = Field()
    # alcohol_content = Field()
    # volatile_acidity = Field()
    # overall_acidity = Field()
    # ph = Field()
    # sugar = Field()
    # bottle_format = Field()
    # production_vinification = Field()
    # climate_soil = Field()

class CarrefourClickSpider(CrawlSpider):
    name = 'carrefour'
    allowed_domains = ['carrefour.es']
    start_urls = ['https://www.carrefour.es/bodega/vinos-tintos/vinos-tintos-nacionales/ver-todos/N-1dxafdm/c',
                  'https://www.carrefour.es/bodega/vinos-blancos/vinos-blancos-nacionales/ver-todos/N-distyh/c',
                  'https://www.carrefour.es/bodega/vinos-rosados/vinos-rosados-nacionales/ver-todos/N-1yz8sfs/c']

# RULES FOR HORIZONTAL & VERTICAL SCROLLING
    rules = (
        Rule(  # RULE1 => HORIZONTAL SCROLLING PER PAGE
            LinkExtractor(
                allow=r'c?No='
            ), follow=True),
        Rule(  # RULE2 => VERTICAL SCROLLING PER WINE PRODUCT
            LinkExtractor(
                allow=r'R-'
            ), follow=True, callback='parse'),
    )

    def parse(self, response):
        item = ItemLoader(WineItems(), response)

        item.add_xpath('winery', '//*[@id="content"]/section/header/p/a/text()')
        item.add_xpath('name', '//h1[@id="product-01"]/text()')
        item.add_xpath('origin', '//*[@id="content"]/section/header/div/p/a/text()')
        item.add_xpath('price', '//*[@id="content"]/section/div[1]/div[3]/p[1]/span[2]/text()')
        item.add_xpath('price_final', '//*[@id="content"]/section/div[1]/div[3]/p[1]/span[2]/text()')
        item.add_xpath('color', '//*[@id="content"]/section/div[1]/div[2]/div/div[1]/div/p/text()')
        item.add_xpath('aging', '//*[@id="content"]/section/div[1]/div[2]/div/div[1]/div[2]/p/text()')
        item.add_xpath('year', '//*[@id="content"]/section/div[1]/div[2]/div/div[2]/div/p/text()')
        item.add_xpath('description', '//*[@id="content"]/section/div[1]/div[2]/div/p/text()')
        item.add_xpath('parker_score', '//*[@id="content"]/section/div[1]/div[2]/div/div[2]/div[1]/p/text()')
        item.add_xpath('testing_view', '//*[@id="content"]/section/div[2]/div[2]/div[2]/div[1]/p[2]/text()')
        item.add_xpath('testing_nose', '//*[@id="content"]/section/div[2]/div[2]/div[2]/div[2]/p[2]/text()')
        item.add_xpath('testing_mouth', '//*[@id="content"]/section/div[2]/div[2]/div[2]/div[3]/p[2]/text()')
        #item.add_xpath('alcohol_content', '/text()')
        #item.add_xpath('volatile_acidity', '/text()')
        #item.add_xpath('alcohol_content', '/text()')
        #item.add_xpath('overall_acidity', '/text()')
        #item.add_xpath('ph', '/text()')
        #item.add_xpath('sugar', '/text()')
        #item.add_xpath('bottle_format', '/text()')
        #item.add_xpath('production_vinification', '/text()')
        #item.add_xpath('climate_soil', '/text()')

        yield item.load_item()

    #def parse_categories(self, response):
        #container_color = response.css("div.column-desc-items")
        #wine_table = response.css("div.item-inner.item-table")
        #dataList = wine_table.css("td.w50")
        #yield {
            #'winery': response.css('p.name-marca.lora a::text').get(),
            #'location': response.css('p.name-formato.lora a::text').get(),
            #'country': 'Spain',
            #'name': response.css('h1.tileDetailBodega.title-03.apercu::text').get(),
            #'color': container_color.css("p::text")[0].get(),
            #'variety': None,
            #'price': response.css('span.js-price-total::text').get(),
            #'rating': None,
            #'body': None,
            #'acidity': self.get_volatile_acidity(dataList),
            #'crawler_day': time.strftime("%Y-%m-%d"),
            #'alcohol_percentage': self.get_alcohol_content(dataList),
            #'editors_choice': None,
            #'id': None,
            #'wine_review_link': None,
            #'wine_review_publish_date': None,
            #'source': "carrefour"
        #}

    #def get_volatile_acidity(self, dataList):
    #    if(re.match(re.compile("\nAcidez\stotal"), dataList.css("p::text")[4].get())):
    #        return dataList.css("p::text")[5].get()
    #    else:
    #        return None

    #def get_alcohol_content(self, dataList):
    #    if(re.match(re.compile("^Graduación\salcohólica"), dataList.css("p::text")[0].get())):
    #        return dataList.css("p::text")[1].get()
    #    else:
    #        return None