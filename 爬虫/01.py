# coding:utf-8

import urllib2

# 修改请求头信息
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}

# urllib2.Request(url,data,headers),构造请求对象
request = urllib2.Request("http://www.baidu.com/",headers=ua_headers)

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
html = response.read()  # 读取文件里的全部内容，返回的是字符串

# 打印响应内容
print(html)

# 打印响应码
print(response.getcode())

# 打印返回页面的URL信息，防止重定向
print(response.geturl())

# 打印服务器响应的HTTP报头信息
print(response.info())