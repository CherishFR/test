# coding:utf-8
import urllib2

# 私密代理需要输入账号密码
httpproxy_handler = urllib2.ProxyHandler({"http": "username:password@122.72.18.35:80"})

opener = urllib2.build_opener(httpproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print(response.read())