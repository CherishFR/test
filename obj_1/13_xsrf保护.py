# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os


from tornado.options import define, options
from tornado.web import RequestHandler, url ,StaticFileHandler

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):
    def get(self):
        self.xsrf_token
        self.render('index.html')
    def post(self):
        pass

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticFileHandler,self).__init__(*args,**kwargs)
        self.xsrf_token
        self.set_secure_cookie('test','abc')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    setting = dict(
        template_path = os.path.join(current_path,"template"),
        cookie_secret = 'rrqUEK3hSgCnknxltqspZXTS2Yu0LEsXr3anyxzG1Mo=',
        xsrf_cookie = True,  # 必须设置cookie_secret
        debug=True,
    )
    app = tornado.web.Application(
        [
            (r"/",IndexHandler),
            (r"/(.*)",StaticFileHandler,{"path": os.path.join(os.path.dirname(__file__),'static1')})
        ],
        **setting
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()