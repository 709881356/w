import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get (self,m):
        m=int(m) if m is not None else 9
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1,m+1):
            html += '<TR>'
            for b in range(1,a+1):
                html +='<TD>%d*%d=%d</TD>' % (a,b,a*b)
            html += '</TR>'
    
        html +='''
        </table>
        </body>
        </html>
        '''
        self.write(html)

application = tornado.web.Application([
    (r"(?:/([0-9])?)", MainHandler),
] )

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
