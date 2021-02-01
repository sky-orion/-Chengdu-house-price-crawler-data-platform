# -*- coding: utf-8 -*-#
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider

from myfirstspyder.items import LianJiaItm

class LianJiaSpider(RedisCrawlSpider):
    name = 'lianjia'
    allowed_domains = ['bj.fang.lianjia.com']
    redis_key = "lianjia:start_urls"

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/ul[2]/li')
        for li in li_list:
            item = LianJiaItm()
            item["url"] = 'https://bj.fang.lianjia.com' + li.xpath('./div/div[1]/a/@href').extract_first()
            yield item