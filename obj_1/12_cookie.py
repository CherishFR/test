# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os


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
    current_path = os.path.dirname(__file__)
    setting = dict(
        static_path=os.path.join(current_path, "static1"),
        template_path=os.path.join(current_path, "template"),
        cookie_secret='rrqUEK3hSgCnknxltqspZXTS2Yu0LEsXr3anyxzG1Mo=',
        xsrf_cookie=True,  # 必须设置cookie_secret
        debug=True,
    )
    app = tornado.web.Application(
        [
            (r"/",IndexHandler),
        ],
        **setting
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()