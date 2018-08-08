# coding:utf-8

import urllib,urllib2

url = "https://www.baidu.com/s?"

wd = {"wd":"天涯明月刀"}

# 将字典数据转换成URL编码格式
url_wd = urllib.urlencode(wd)
print(url_wd)

# 转换回去
new_wd = urllib.unquote(url_wd)
print(new_wd)

# 发送get请求
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

keyword = raw_input("请输入需要查询的字符串：")
wd = {"wd":keyword}
wd = urllib.urlencode(wd)
fullurl = url + "?" + wd

request = urllib2.Request(fullurl,headers=ua_headers)

response = urllib2.urlopen(request)

print(response.read())