# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyfirstspyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LianJiaItm(scrapy.Item):
    url = scrapy.Field()

class LianJiaDetail(scrapy.Item):
    data_project_name = scrapy.Field()
    unitPriceValue = scrapy.Field()
    unit1 = scrapy.Field()
    totalPriceValue = scrapy.Field()
    unit2 = scrapy.Field()
    huxing1 = scrapy.Field()
    mianji1 = scrapy.Field()
    huxing2 = scrapy.Field()
    mianji2 = scrapy.Field()
    huxing3 = scrapy.Field()
    mianji3 = scrapy.Field()
