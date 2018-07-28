# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb
import json,os


from tornado.options import define ,options
from tornado.web import RequestHandler ,url
from tornado.websocket import WebSocketHandler

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):
    def get(self):
        self.render('webchat.html')

class ChatHandler(WebSocketHandler):
    users = set()

    def open(self):
        """当一个WebSocket连接建立后被调用"""
        self.users.add(self)
        for user in self.users:
            user.write_massage("%s上线了" % self.request.remote_ip)
        print("%s上线了" %self.request.remote_ip)


    def on_message(self, message):
        """当客户端发送message消息过来时被调用"""
        for user in self.users:
            user.write_massage('%s说：%s' % (self.request.remote_ip,message))

    def on_close(self):
        """当WebSocket连接关闭后被调用"""
        self.users.remove(self)
        for user in self.users:
            user.write_massage("%s已离开" % self.request.remote_ip)
        print("%s已离开" %self.request.remote_ip)

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application, self).__init__(*args,**kwargs)
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="aijia",
            user="liu",
            password="Jm25csdb."
        )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    setting = dict(
        static_path=os.path.join(current_path, "static1"),
        debug=True,
    )
    app = Application(
        [
            (r"/",IndexHandler),
            (r"/chat",ChatHandler),
        ],
        **setting
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()