# coding:utf-8
import urllib2

# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
# http_handler = urllib2.HTTPHandler()

# 在HTTPHandler增加参数“debuglevel=1”将会自动打开Debug log模式，程序执行时会打印收发包信息
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 调用build_opener()方法构建一个自定义的opener发送请求
opener = urllib2.build_opener(http_handler)

request = urllib2.Request("http://www.baidu.com/")

response = opener.open(request)
print(response.read())