# coding:utf-8

import urllib2
import re

class Spider:
    def __init__(self):
        # 初始化起始页的位置
        self.page = 1
        # 爬取开关，如果为True就继续爬取
        self.switch = True

    def loadPage(self,page):
        """下载页面"""
        _url = "http//www.neihan8.com/article/list_5_" + str(page) + ".html"
        _headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
        _request = urllib2.Request(_url,headers=_headers)
        _response = urllib2.urlopen(_request)

        # 获取每一页HTML的源码字符串
        _html = _response.read()

        # 创建一个正则表达式匹配规则，匹配<div class="f18 mb20"><\div>这个标签里的内容，re.S表示匹配全部内容
        _pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)

        # 将正则匹配对象应用到html源码字符串里，返回这个页面里所有被匹配的内容
        _content_list = _pattern.findall(_html)
        self.dealPage(_content_list)
        # for content in content_list:
        #     # 如果内容是gbk格式，则需要进行解码
        #     print(content.decode("gbk"))


    def dealPage(self,_content_list):
        """处理每一页的数据"""
        for _item in _content_list:
            # 将数据内没用的东西替换成空字符串
            _item = _item.replace("<p>","").replace("</p>","").replace("<br>","").replace("<br />","")
            self.writePage(_item)

    def writePage(self,_item):
        """把需要的数据逐个写入文件"""
        with open("data.txt","a") as f:
            f.write(_item)

    def startWork(self):
        """控制爬虫运行"""
        while self.switch:
            _command = raw_input("如果继续爬取请按回车，退出输入quit")
            if _command == "quit":
                self.switch = False
            self.loadPage(self.page)
            self.page += 1


if __name__ == '__main__':
    testSpider = Spider()
    testSpider.startWork()