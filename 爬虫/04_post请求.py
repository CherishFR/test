# coding:utf-8
import urllib2,urllib

# 真实请求的地址，通过抓包获取
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

#完整的请求头
headers = {
    "Host": "fanyi.youdao.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8"
        }

key = raw_input("请输入需要翻译的英文：")

# 通过Form表单发送到web服务器的数据
formdata = {
    "i":key,
    "from":"en",
    "to":"zh-CHS",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1533735232525",
    "sign":"e917cda162c9dea481266a0766af3444",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false",
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url,data=data,headers=headers)

response = urllib2.urlopen(request)
print(response.read())