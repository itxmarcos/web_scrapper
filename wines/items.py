# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class WinesItem(Item):
    # define the fields for your item here like:
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