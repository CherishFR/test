# coding:utf-8
import tornado.web
import tornado.ioloop



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello tornado')


if __name__ == '__main__':
    app = tornado.web.Application([(r"/",IndexHandler)])  # 类似于Django的url
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()