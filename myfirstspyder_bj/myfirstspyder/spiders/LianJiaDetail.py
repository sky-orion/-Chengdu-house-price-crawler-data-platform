# -*- coding: utf-8 -*-#

from scrapy_redis.spiders import RedisCrawlSpider

from myfirstspyder.items import LianJiaItm, LianJiaDetail

class LianJiaDetailSpider(RedisCrawlSpider):
    name = 'LianJiaDetailSpider'
    allowed_domains = ['bj.fang.lianjia.com']
    redis_key = "lianjia:detail_urls"

    def parse(self, response):
        item = LianJiaDetail()
        item["data_project_name"] = response.xpath('//div[2]/div[2]/div[1]/div[1]/h2/text()').extract_first()
        item["unitPriceValue"] = response.xpath('//div[2]/div[3]/div[2]/div/div[2]/div[1]/span[2]/text()').extract_first()
        item["unit1"] = response.xpath('//div[2]/div[3]/div[2]/div/div[2]/div[1]/span[3]/text()').extract_first()
        item["totalPriceValue"] = response.xpath('//div[2]/div[3]/div[2]/div/div[2]/div[1]/span[4]/text()').extract_first()
        item["unit2"] = response.xpath('//div[2]/div[3]/div[2]/div/div[2]/div[1]/span[5]/text()').extract_first()
        item["huxing1"] = response.xpath('//div[2]/div[6]/div/div[2]/div[1]/ul/li[2]/ul[1]/div[2]/div[1]/text()').extract_first()
        item["mianji1"] = response.xpath('//div[2]/div[6]/div/div[2]/div[1]/ul/li[2]/ul[1]/div[2]/div[2]/text()').extract_first()
        item["huxing2"] = response.xpath('//div[2]/div[6]/div/div[2]/div[1]/ul/li[2]/ul[2]/div[2]/div[1]/text()').extract_first()
        item["mianji2"] = response.xpath('//div[2]/div[6]/div/div[2]/div[1]/ul/li[2]/ul[2]/div[2]/div[2]/text()').extract_first()
        item["huxing3"] = response.xpath('//div[2]/div[6]/div/div[2]/div[1]/ul/li[2]/ul[3]/div[2]/div[1]/text()').extract_first()
        item["mianji3"] = response.xpath('//div[2]/div[6]/div/div[2]/div[1]/ul/li[2]/ul[3]/div[2]/div[2]/text()').extract_first()
        yield item