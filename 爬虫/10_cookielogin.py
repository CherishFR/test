# coding:utf-8
import urllib2,urllib
import cookielib

# 通过CookieJar()构建一个CookieJar对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_handler)

# 自定义opener的addheaders的参数，可以添加HTTP报头参数,以元组的格式发送，键值对用,隔开
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")]

# 人人网登陆接口
url = "http://www.renren.com/PLogin.do"

# 需要登陆的账户密码
data = {"email":"username","password":"passwd"}

data = urllib.urlencode(data)

# 第一次post请求，发送登陆需要的参数，获取cookie
request = urllib2.Request(url,data=data)

response = opener.open(request)

print(response.read())

# 第二次请求会携带cookie信息，用来获取登陆后才能获取的信息