# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import redis
from itemadapter import ItemAdapter

from myfirstspyder.items import LianJiaItm, LianJiaDetail

def write_redis(redis_obj, item):
    redis_obj.rpush("lianjia:detail_urls", item["url"])

class MyfirstspyderPipeline:
    # 初始化redis连接
    def __init__(self):
        # 创建连接池
        pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024)
        # 创建连接对象
        coon = redis.Redis(connection_pool=pool)
        self.redis_obj = coon

    def process_item(self, item, spider):
        if isinstance(item, LianJiaItm):
            write_redis(self.redis_obj, item)
        elif isinstance(item, LianJiaDetail):
            data_project_name = item["data_project_name"]
            unitPriceValue = item["unitPriceValue"]
            unit1 = item["unit1"]
            totalPriceValue = item["totalPriceValue"]
            unit2 = item["unit2"]
            huxing1 = item["huxing1"]
            mianji1 = item["mianji1"]
            huxing2 = item["huxing2"]
            mianji2 = item["mianji2"]
            huxing3 = item["huxing3"]
            mianji3 = item["mianji3"]
            with open("链家北京新房.txt", "a+", encoding='utf-8') as f:
                f.write("{},".format(data_project_name))
                f.write("{},".format(unitPriceValue))
                f.write("{},".format(unit1))
                f.write("{},".format(totalPriceValue))
                f.write("{},".format(unit2))
                f.write("{},".format(huxing1))
                f.write("{},".format(mianji1))
                f.write("{},".format(huxing2))
                f.write("{},".format(mianji2))
                f.write("{},".format(huxing3))
                f.write("{}\n".format(mianji3))