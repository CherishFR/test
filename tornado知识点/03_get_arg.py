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
    ''' 主页处理类 '''
    def get(self):
        # subject = self.get_query_argument("subject")  # 对重复参数只取最后一个
        query_args = self.get_query_arguments("s")  # 取出所有重复参数
        body_arg = self.get_body_argument("s")
        body_args = self.get_body_argument("s")
        arg = self.get_argument('s')
        args = self.get_arguments('s')
        json_data = self.request.body  # 拿到jsonbody的字符串
        json_args = json.load(json_data)  # 转化为json参数
        self.write(str(query_args))


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