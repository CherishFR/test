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
    def get(self):
        stu = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        # stu_json = json.dumps(stu)  # 如果手动进行json序列化操作，那响应头header中Content-Type字段为text/html;
        self.write(stu)  # 字典会自动转化为json格式进行传输，此时响应头header中Content-Type字段变成application/json;
        self.set_header("Content-Type", "text/html; charset=UTF-8")  # 当然我们可以人为干预Content-Type字段
        self.set_status(404)  # 设置状态码，虽然network会报错，但是还是能拿到数据

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