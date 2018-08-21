# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
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

        if self.offset < 3320:
            self.offset += 10

        # 每次处理完一页重新发送请求处理下一页
        # 将请求重新发送给调度器：入队列，出队列，交给下载其下载
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)