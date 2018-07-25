# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver


from tornado.options import define, options
from tornado.web import RequestHandler, url

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):
    def get(self):
        if not self.get_cookie('user'):
            self.set_cookie('user','admin')
        print("调用了get()")


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