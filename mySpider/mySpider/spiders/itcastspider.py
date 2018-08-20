# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

# 创建爬虫的类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "Itcast"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫起始的url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        # 通过scrapy自带的xpath匹配出所有老师的根节点，结果为列表
        teacher_list = response.xpath('//div[@class="li_txt"]')

        # 所有老师信息的列表集合
        # teacherItem = []
        # 遍历根节点的列表集合
        for each in teacher_list:
            # item对象用来保存数据
            item = ItcastItem()
            # 名字,extract()将匹配的内容转化成Unicode字符串，否则结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            # 职称
            title = each.xpath('./h4/text()').extract()
            # 介绍
            info = each.xpath('./p/text()').extract()

            item["name"]= name[0]
            item["title"]= title[0]
            item["info"]= info[0]
            # teacherItem.append(item)

            # 通过yield将数据传给pipelines文件，pipelines文件继续处理数据
            yield item

        # return teacherItem