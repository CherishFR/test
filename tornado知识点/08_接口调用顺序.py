# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver

import json

from tornado.options import define ,options
from tornado.web import RequestHandler ,url

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):

    def initialize(self):
        print("调用了initialize()")

    def prepare(self):
        print("调用了prepare()")

    def set_default_headers(self):
        print("调用了set_default_headers()")

    def write_error(self, status_code, **kwargs):
        print("调用了write_error()")

    def get(self):
        print("调用了get()")

    def post(self):
        print("调用了post()")
        self.send_error(200)  # 注意此出抛出了错误

    def on_finish(self):
        print("调用了on_finish()")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/",IndexHandler),
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()