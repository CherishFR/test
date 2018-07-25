# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torndb


from tornado.options import define ,options
from tornado.web import RequestHandler ,url

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class InsertHandler(RequestHandler):
    def post(self):
        h_title = self.get_argument("title")
        h_position = self.get_argument("position")
        h_price = self.get_argument("price")
        sql = "insert into aj_house_info(hi_title,hi_position,hi_price) value (%(h_title)s,%(h_position)s,%(h_price)s)"
        try:
            ret = self.application.db.execute(sql, h_title=h_title, h_position=h_position, h_price=h_price)
        except Exception as e:
            self.write("DB error:%s" % e)
        else:
            self.write("OK %d" % ret)

class HouseHandler(RequestHandler):
    def get(self):
        hid = self.get_argument("id")
        sql = "select hi_title,hi_position ,hi_price from aj_house_info where id=%s"
        try:
            ret = self.application.db.get(sql,hid)
        except Exception as e:
            self.write("DB error:%s" % e)
        else:
            print(type(ret))
            print(ret)
            print(ret.title)
            print(ret['title'])
            self.render("index.html", houses=[ret])

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application, self).__init__(*args,**kwargs)
        # 创建一个全局mysql连接实例供handler使用
        self.db = torndb.Connection(
            host="127.0.0.1",
            database="aijia",
            user="root",
            password="Jm25csdb."
        )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r"/insert",InsertHandler),
            (r"/house",HouseHandler),
        ],
        debug=True
    )
    # app.db = torndb.Connection(
    #     host="127.0.0.1",
    #     database="aijia",
    #     user="root",
    #     password="Jm25csdb."
    # )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()