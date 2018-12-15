
#wsgi_server应该能和任意wsgi_frame无缝衔接
#wsgi_frame应该能适应任意wsgi_server

"""
web框架是一个骨架，是对web开发的核心和公共部分的抽象。是模板。
它做一些每个web项目的重复部分:(与业务无关的功能性部分)

大多数web框架包含模式和工具，至少实现以下功能：

1.URL路由（URL Routing）
    将输入的HTTP请求匹配到特定的Python代码用来调用
2.请求和响应对象（Request and Response Objects）
    封装来自或发送给用户浏览器的信息
3.模板引擎（Template Engine）
    能够将实现应用的Python代码逻辑和其要产生输出的HTML（或其他）分离开
4.Web服务器开发（Development Web Server）
    在开发机上运行HTTP服务器，从而快速开发；当文件更新时自动更新服务端代码。

"""
from functools import wraps
import cgi, pdb

class App(object):
    def __init__(self):
        self.path_mapping = {}

    # 服务器对 application的调用协议: application(environ, start_response)
    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
##        pdb.set_trace()
        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        
        # 从请求中提取查询参数并将它们放入一个类字典对象中
        environ['params'] = { key: params.getvalue(key) for key in params }

        ## 请求分发
        handler = self.path_mapping.get((method,path), self.notfound_404)
        return handler(environ, start_response)
    
    def notfound_404(self, environ, start_response):
        start_response('404 Not Found', [ ('Content-type', 'text/plain') ])
        return [b'Not Found']

    def route(self, method, url):
        def decorator(handler):
            self.path_mapping[(method,url)] = handler
##            pdb.set_trace()
##            @wraps(handler)
##            def wrapper(*args, **kwargs):
##                return handler(*args, **kwargs)
##            return wrapper
            return handler
        return decorator

# handler 示例
##@app.route("get", "sayhi") 
##def sayhi():
##    pass


if __name__ == '__main__':
    # 不知道 App怎么写，那可以先看看它如何被使用
    application = App()
    from wsgiref.smple_server import make_server
    #TODO 不应该由 web_frame来启动程序!
    PORT = 8088
    httpd = make_server(('0.0.0.0',PORT), application)
    # 服务器会将所有请求都交给application处理，所有分发请求时要注意区分出静态资源请求
    # 服务器对 application的调用协议: application(environ, start_response)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()
