# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ItcastPipeline(object):
    # __init__可选，作为类的初始化方法
    def __init__(self):
        # 创建了一个文件
        self.filename = open('teacher.json','w')

    # process_item方法是必须写的，处理item数据
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))

    # close_spider可选，最后执行，做一些收尾工作
    def close_spider(self, spider):
        self.filename.close()