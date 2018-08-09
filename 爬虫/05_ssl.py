# coding:utf-8
import urllib2,ssl

url = "https://www.12306.cn/mormhweb/"

# 忽略ssl安全认证
context = ssl._create_stdlib_context()

request = urllib2.Request(url)

response = urllib2.urlopen(request,context)

print(response.read())