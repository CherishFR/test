# coding:utf-8

import urllib2,urllib,random

ua_header = [
    {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"},
    {"User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"},
    {"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0"},
    {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}
]

def loadPage(url,filename):
    """
    根据url发送请求，获取服务器响应文件
    url：需要爬取的url地址
    filename：文件名
    """
    print("正在下载"+filename)
    header = random.choice(ua_header)
    request = urllib2.Request(url,headers=header)
    response = urllib2.urlopen(request)
    return response.read()


def writePage(html,filename):
    """
    将html内容写入到本地
    html：服务器响应文件的内容
    """
    print("正在保存"+filename)
    filename = filename +".html"
    with open(filename,"w") as f:
        f.write(html)

def tiebaSpider(url,beginPage,endPage):
    """
    贴吧爬虫调度器，负责组合处理每个页面的url
    url: url地址前缀
    beginPage: 起始页
    endPage: 终止页
    """
    for page in range(beginPage,endPage + 1):
        pn = str((page-1) *50)
        filename = "第%s页" %page
        fullurl = url + "&pn=" + pn
        html = loadPage(fullurl,filename)
        writePage(html,filename)

if __name__ == '__main__':
    kw = raw_input("请输入需要爬取的贴吧名：")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    url_kw = urllib.urlencode({"kw":kw})
    fullurl = url +url_kw
    tiebaSpider(fullurl,beginPage,endPage)