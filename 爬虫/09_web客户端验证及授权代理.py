# coding:utf-8
import urllib2

# 在站点需要授权信息的时候使用
test = "test"
password = "123456"
webserver = "192.168.10.10"

# 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息，第一个参数realm如果没有指定就写None，后三个参数为站点IP，账户，密码
passwordMgr.add_password(None,webserver,test,password)

# HTTPBasicAuthHandler()HTTP基础验证处理器类
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)
# 处理代理基础验证相关的处理器类
# proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwordMgr)

opener = urllib2.build_opener(httpauth_handler)

request = urllib2.Request("http://" + webserver)
response = opener.open(request)
print(response.read())