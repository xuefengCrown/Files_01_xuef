
import time
from bottle_v1 import route, run # 导入框架

_hello_resp = '''\
<html>
  <head>
     <title>Hello {name}</title>
   </head>
   <body>
     <h1>Hello {name}!</h1>
   </body>
</html>'''

import pdb
##start_response 参数是一个为了初始化一个请求对象而必须被调用的函数。
##第一个参数是返回的HTTP状态值，第二个参数是一个(名,值)元组列表，用来构建返回的HTTP头。
@route("/sayhi") # 默认 get方法
def hello_world(req, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = req.params
    #pdb.set_trace()

    # 相当于极简单的模板引擎
    resp = _hello_resp.format(name=params.get('name'))
    
    #为了返回数据，一个WSGI程序必须返回一个字节字符串序列。
    # 当然，并没有要求你返回的一定是文本，你可以很轻松的编写一个生成图片的程序。
    yield resp.encode('utf-8')

_localtime_resp = '''\
<?xml version="1.0"?>
<time>
  <year>{t.tm_year}</year>
  <month>{t.tm_mon}</month>
  <day>{t.tm_mday}</day>
  <hour>{t.tm_hour}</hour>
  <minute>{t.tm_min}</minute>
  <second>{t.tm_sec}</second>
</time>'''

@route("/localtime") 
def localtime(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/xml') ])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':
    #run(server=WSGIRefServer, host='127.0.0.1', port=8080, optinmize = False, **kargs)
    run(port = 8090)

    
