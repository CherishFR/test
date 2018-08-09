# coding:utf-8
import urllib2

# 代理开关，是否启用代理
Proxyswitch = True

# 构建一个Handler处理器对象，参数是字典类型，包括代理类型，代理服务器IP以及端口
httpproxy_handler = urllib2.ProxyHandler({"http": "122.72.18.35:80"})

# 构建一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if Proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print(response.read())