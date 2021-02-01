# -*- coding: utf-8 -*-#

import redis

# 创建连接池
pool = redis.ConnectionPool(host="localhost", port=6379, max_connections=1024)
# 创建连接对象
coon = redis.Redis(connection_pool=pool)
print("开始...")
for i in range(1, 22):
    url = "https://bj.fang.lianjia.com/loupan/pg{}/".format(i)
    coon.lpush("lianjia:start_urls", url)
print("结束...")
