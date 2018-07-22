# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os

from tornado.options import define ,options
from tornado.web import RequestHandler ,StaticFileHandler

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class HiHandler(RequestHandler):
    def get(self):
        self.write("hi")

class IndexHandler(RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application(
        [
            (r"/", IndexHandler),
            (r"/api/hi",HiHandler),  # 约定所有的接口以api开头
            (r"/(.*)", StaticFileHandler,{
                "path": os.path.join(current_path, "static/html"),
                "default_filename": "index.html"
            }),  # 模糊匹配的放在最下面
        ],
        static_path=os.path.join(current_path, "static"),
        template_path=os.path.join(current_path, "template"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()