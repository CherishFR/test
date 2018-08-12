# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb
import json


from tornado.options import define ,options
from tornado.web import RequestHandler ,url
from tornado.httpclient import AsyncHTTPClient

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):

    # @tornado.web.asynchronous
    # def get(self):
    #     client = AsyncHTTPClient()
    #     client.fetch(
    #         'http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=218.192.3.42',
    #         callback=self.on_response
    #     )
    #
    # def on_response(self,resp):
    #     json_data = resp.body
    #     data = json.load(json_data)
    #     self.write(data)
    #     self.finish()
    @tornado.gen.coroutine
    def get(self):
        client = AsyncHTTPClient()
        resp = yield client.fetch('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=218.192.3.42')
        json_data = resp.body
        data = json.load(json_data)
        raise tornado.gen.Return(data)


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
    app = Application(
        [
            (r"/",IndexHandler),
        ],
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()