# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json

from tornado.options import define ,options
from tornado.web import RequestHandler ,url

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):
    def set_default_headers(self):
        # 设置get与post方式的默认响应体格式为json
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置一个名为itcast、值为python的header
        self.set_header("itcast", "python")

    def get(self):
        stu = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("itcast", "i love python")  # 注意此处重写了header中的itcast字段

    def post(self):
        stu = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)

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