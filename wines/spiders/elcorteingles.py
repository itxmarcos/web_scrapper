from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

"""
Command to scrape --> scrapy crawl elcorteingles -o carrefour.csv
Fortunately ElCorteIngles' web is not provided with anticrawler blocking for Scrapy: https://www.elcorteingles.es/robots.txt
"""

class WineItems(Item):
    winery = Field()
    name = Field()
    origin = Field()
    price = Field()
    price_final = Field()
    #color = Field()
    #aging = Field()
    #year = Field()
    #description = Field()
    #parker_score = Field()
    #testing_view = Field()
    #testing_nose = Field()
    #testing_mouth = Field()
    # alcohol_content = Field()
    # volatile_acidity = Field()
    # overall_acidity = Field()
    # ph = Field()
    # sugar = Field()
    # bottle_format = Field()
    # production_vinification = Field()
    # climate_soil = Field()

class ElcorteinglesClickSpider(CrawlSpider):
    name = 'elcorteingles'
    allowed_domains = ['elcorteingles.es']
    start_urls = ['https://www.elcorteingles.es/club-del-gourmet/vinos/espana/attr.basegourmet_type_list::Tinto/',
                  'https://www.elcorteingles.es/club-del-gourmet/vinos/espana/attr.basegourmet_type_list::Blanco/',
                  'https://www.elcorteingles.es/club-del-gourmet/vinos/espana/attr.basegourmet_type_list::Rosado/']

# RULES FOR HORIZONTAL & VERTICAL SCROLLING
    rules = (
        Rule(  # RULE1 => HORIZONTAL SCROLLING PER PAGE
            LinkExtractor(
                allow=r'\d+/'
            ), follow=True),
        Rule(  # RULE2 => VERTICAL SCROLLING PER WINE PRODUCT
            LinkExtractor(
                allow=r'club-del-gourmet/A'
            ), follow=True, callback='parse'),
    )

    def parse(self, response):
        item = ItemLoader(WineItems(), response)

        item.add_xpath('winery', '//*[@id="tab-content-0"]/div/dl[1]/div[2]/dd/text()')
        item.add_xpath('name', '//*[@id="product-detail-container"]/div[1]/div[2]/div/div[1]/div[2]/text()')
        item.add_xpath('origin', '//*[@id="tab-content-0"]/div/dl[1]/div[3]/dd/text()')
        item.add_xpath('price', '//*[@id="product-detail-container"]/div[1]/div[2]/div/div[4]/div/p[2]/text()')
        item.add_xpath('price_final', '//*[@id="product-detail-container"]/div[1]/div[2]/div/div[4]/div/p[1]/span[1]/text()')
        #item.add_xpath('color', '//*[@id="content"]/section/div[1]/div[2]/div/div[1]/div/p/text()')
        #item.add_xpath('aging', '//*[@id="content"]/section/div[1]/div[2]/div/div[1]/div[2]/p/text()')
        #item.add_xpath('year', '//*[@id="content"]/section/div[1]/div[2]/div/div[2]/div/p/text()')
        #-item.add_xpath('description', '//*[@id="product-detail-container"]/div[1]/div[1]/div/div[3]/text()')
        #item.add_xpath('parker_score', '//*[@id="content"]/section/div[1]/div[2]/div/div[2]/div[1]/p/text()')
        #item.add_xpath('testing_view', '//*[@id="content"]/section/div[2]/div[2]/div[2]/div[1]/p[2]/text()')
        #item.add_xpath('testing_nose', '//*[@id="content"]/section/div[2]/div[2]/div[2]/div[2]/p[2]/text()')
        #item.add_xpath('testing_mouth', '//*[@id="content"]/section/div[2]/div[2]/div[2]/div[3]/p[2]/text()')
        #item.add_xpath('alcohol_content', '/text()')
        #item.add_xpath('volatile_acidity', '/text()')
        #-item.add_xpath('alcohol_content', '//*[@id="tab-content-0"]/div/dl[1]/div[6]/dd/text()')
        #item.add_xpath('overall_acidity', '/text()')
        #item.add_xpath('ph', '/text()')
        #item.add_xpath('sugar', '/text()')
        #item.add_xpath('bottle_format', '/text()')
        #-item.add_xpath('production_vinification', '//*[@id="tab-content-0"]/div/dl[1]/div[7]/dd/text()')
        #item.add_xpath('climate_soil', '/text()')

        yield item.load_item()
