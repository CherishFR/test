# coding:utf-8
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib
import xmltodict
import time
import tornado.gen
import json
import os

from tornado.web import RequestHandler
from tornado.options import options,define
from tornado.httpclient import AsyncHTTPClient,HTTPRequest

WECHAT_TOKEN = "liu"
WECHAT_APPID = "wx665796ccc23a5a33"
WECHAT_APP_SECRET = "e96fa5369898a454b0453bed204b9596"

define("port",default=8000,type=int,help="")

class AccessToken(object):
    """access_token辅助类，access_token是公众号的全局唯一票据，公众号调用各接口时都需使用access_token。"""
    _access_token = None
    _create_time = 0
    _expires_in = 0

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APPID, WECHAT_APP_SECRET)
        resp = yield client.fetch(url)
        dict_data = json.load(resp.body)
        if "errcode" in dict_data:
            raise Exception("wechat server error")
        else:
            cls._access_token = dict_data["access_token"]
            cls._expires_in = dict_data["expires_in"]
            cls._create_time = time.time()

    @classmethod
    @tornado.gen.coroutine
    def get_access_token(cls):
        if time.time() - cls._create_time > (cls._expires_in -200):
            # 当前时间-创建时间 > 凭证有效期，即凭证过期
            yield cls.update_access_token()
            raise tornado.gen.Return(cls._access_token)
        else:
            raise tornado.gen.Return(cls._access_token)

class QrcodeHandler(RequestHandler):
    """
    请求微信服务器，生成带参数的二维码
    获取带参数的二维码的过程包括两步，首先创建二维码ticket，然后凭借ticket到指定URL换取二维码。
    """
    @tornado.gen.coroutine
    def get(self):
        scene_id = self.get_argument("sid")
        try:
            access_token = yield AccessToken.get_access_token()  # 获取凭证，由于上面是异步因此需要写yield
        except Exception as e:
            self.write("errmsg:%s" % e)
        else:
            client = AsyncHTTPClient()
            url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
            req_data = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": scene_id}}}  # 请求永久二维码
            req = HTTPRequest(
                url=url,
                method="POST",
                body=json.dump(req_data)
            )
            resp = yield client.fetch(req)  # 到指定URL请求ticket
            dict_resp = json.loads(resp.body)
            if "errcode" in dict_resp:
                self.write("errmsg:get qrcode failed")
            else:  # 获取ticket后，根据ticket请求二维码，用<img>标签显示出来
                ticket = dict_resp["ticket"]
                qrcode_url = dict_resp["url"]
                self.write('<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s"><br/>' % ticket)
                self.write('<p>%s</p>' % qrcode_url)


class WechatHandler(RequestHandler):
    def prepare(self):
        """
        对接微信服务器
            流程：
                1.将token, timestamp, nonce三个参数进行字典序排序。
                2.将三个字符串拼接成一个字符串进行sha1加密。
                3.将加密后的字符串与signature比对，一致则说明请求来自微信。
        """
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp = "".join(tmp)
        real_signature = hashlib.sha1(tmp).hexsdigest()
        if signature != real_signature:
            self.write_error(403)

    def get(self):
        echostr = self.get_argument("echostr")
        self.write(echostr)

    def post(self,):
        xml_data = self.request.body
        dict_data = xmltodict.parse(xml_data)
        msg_type = dict_data["xml"]["MsgType"]
        if msg_type == "test":
            content = dict_data["xml"]["Content"]
            resp_data = {
                'xml':{
                    "ToUserName":dict_data["xml"]["FromUserName"],
                    "FromUserName":dict_data["xml"]["ToUserName"],
                    "CreateTime":int(time.time()),
                    "MsgType":"text",
                    "Content":content
                }
            }
            self.write(xmltodict.unparse(resp_data))
        elif msg_type == "event":
            if dict_data['xml']['Event'] == "subscribe":
                """用户关注的事件"""
                resp_data = {
                    'xml':{
                        "ToUserName":dict_data["xml"]["FromUserName"],
                        "FromUserName":dict_data["xml"]["ToUserName"],
                        "CreateTime":int(time.time()),
                        "MsgType":"text",
                        "Content":u"感谢关注"
                    }
                }
                if "EventKey" in dict_data['xml']:
                    """通过二维码关注"""
                    eventkey = dict_data['xml']['EventKey']
                    scene_id = eventkey[8:]
                    resp_data['xml']['Content'] = u"感谢关注"+scene_id
                self.write(xmltodict.unparse(resp_data))
            elif dict_data['xml']['Event'] == "SCAN":
                """如果扫描二维码的用户已经关注"""
                scene_id = dict_data['xml']['EventKey']
                resp_data = {
                    'xml': {
                        "ToUserName": dict_data["xml"]["FromUserName"],
                        "FromUserName": dict_data["xml"]["ToUserName"],
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": u"已关注"+scene_id
                    }
                }
                self.write(xmltodict.unparse(resp_data))
        else:
            resp_data = {
                'xml': {
                    "ToUserName": dict_data["xml"]["FromUserName"],
                    "FromUserName": dict_data["xml"]["ToUserName"],
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "hahaha"
                }
            }
            self.write(xmltodict.unparse(resp_data))


class ProfileHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        code = self.get_argument("code")
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (WECHAT_APPID,WECHAT_APP_SECRET,code)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body)
        if "errcode" in dict_data:
            self.write("error occur")
        else:
            access_toke = dict_data['access_toke']
            open_id = dict_data['openid']
            url = "https://api.weixin.qq.com/sns/userinfo?access_token=$s&openid=%s&lang=zh_CN" %(access_toke,open_id)
            resp = yield client.fetch(url)
            user_data = json.loads(resp.body)
            if "errcode" in dict_data:
                self.write("error occur again")
            else:
                self.render("index.html",user_data)


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/wechat",WechatHandler),
            (r"/qrcode",QrcodeHandler),
            (r"/profile",ProfileHandler)
        ],
        template_path= os.path.join(os.path.dirname(__file__),"template"),
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()