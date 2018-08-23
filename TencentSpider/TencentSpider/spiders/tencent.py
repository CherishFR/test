# -*- coding: utf-8 -*-
import scrapy
# 导入CrawlSpider类和Rule规则
from scrapy.spiders import CrawlSpider,Rule
# 导入链接规则匹配，用来提取规则的链接
from scrapy.linkextractors import LinkExtractor
from TencentSpider.items import TencentItem

class TencentSpoder(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象列表
    pagelink = LinkExtractor(allow=("start=\d+"))
    rules = [
        # 获取这个列表的链接，依次发送请求，并且继续跟进，调用指定的回调函数处理
        Rule(pagelink,callback='parseTencent', follow= True)
    ]

    def parseTencent(self,response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 初始化模型对象
            item = TencentItem()
            # 职位名称
            item["sitionname"] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            item["positionlink"] = each.xpath("./td[1]/a/@href").extract()[0]
            # 类别
            item["positiontype"] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item["perpleNum"] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item["workLocation"] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item["publishTime"] = each.xpath("./td[5]/text()").extract()[0]

            # 将数据给管道文件处理
            yield item
