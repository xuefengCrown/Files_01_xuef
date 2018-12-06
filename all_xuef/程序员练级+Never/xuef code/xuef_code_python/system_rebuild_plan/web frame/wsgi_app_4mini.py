"""
例如，长期运行的程序可能会使用一个REST API来实现监控或诊断。
大数据应用程序可以使用REST来构建一个数据查询或提取系统。
REST还能用来控制硬件设备比如机器人、传感器、工厂或灯泡。
更重要的是，REST API已经被大量客户端编程环境所支持，比如Javascript, Android, iOS等。
因此，利用这种接口可以让你开发出更加复杂的应用程序。

"""
import time
from mini_webframe import App # 导入框架

_hello_resp = '''\
<html>
  <head>
     <title>Hello {name}</title>
   </head>
   <body>
     <h1>Hello {name}!</h1>
   </body>
</html>'''

app = App()

##start_response 参数是一个为了初始化一个请求对象而必须被调用的函数。
##第一个参数是返回的HTTP状态值，第二个参数是一个(名,值)元组列表，用来构建返回的HTTP头。
@app.route("get", "/sayhi") 
def hello_world(environ, start_response):
    start_response('200 OK', [ ('Content-type','text/html')])
    params = environ['params']

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

@app.route("get", "/localtime") 
def localtime(environ, start_response):
    start_response('200 OK', [ ('Content-type', 'application/xml') ])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':

    from wsgiref.simple_server import make_server # basic server

    # Create the dispatcher and register functions
##    dispatcher = PathDispatcher()
##    dispatcher.register('GET', '/hello', hello_world)
##    dispatcher.register('GET', '/localtime', localtime)

    
    port = 8088
    # Launch a basic server
    httpd = make_server('', port, app)
    print('Serving on port {port}...'.format(port=port))
    httpd.serve_forever()


    
