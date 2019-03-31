import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("tg912")
        print("tanggasdf")
        print("tg9123S")
        print("tanggang9")
        self.write("Hello world")


class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)


class BuyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("buy.wupeiqi.com/index")


application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/story/([0-9])",StoryHandler),
])

application.add_handlers("buy.wupeiqi.com$",[
    (r"/index",BuyHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
