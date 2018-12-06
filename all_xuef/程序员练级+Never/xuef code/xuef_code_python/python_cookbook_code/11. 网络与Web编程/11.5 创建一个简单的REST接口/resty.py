"""
为了实现一个简单的REST接口，你只需让你的程序代码满足Python的WSGI标准即可。
WSGI被标准库支持，同时也被绝大部分第三方web框架支持。
因此，如果你的代码遵循这个标准，在后面的使用过程中就会更加的灵活！
"""

# resty.py
## 相当于一个小型 web frame
"""
WSGI本身是一个很小的标准。因此它并没有提供一些高级的特性比如认证、cookies、重定向等。
这些你自己实现起来也不难。
不过如果你想要更多的支持，可以考虑第三方库，比如 WebOb 或者 Paste
"""
import cgi
import pdb

def notfound_404(environ, start_response):
    start_response('404 Not Found', [ ('Content-type', 'text/plain') ])
    return [b'Not Found']

# 尽管WSGI程序通常被定义成一个函数，不过你也可以使用类实例来实现，
# 只要它实现了合适的 __call__() 方法。
# 这个分发器仅仅只是管理一个字典，将(方法,路径)对映射到处理器函数上面。
# 当一个请求到来时，它的方法和路径被提取出来，然后被分发到对应的处理器上面去。
# 最后，使用WSGI还有一个很重要的部分就是没有什么地方是针对特定web服务器的。
class PathDispatcher:
    def __init__(self):
        self.pathmap = { }

    # environ 属性是一个字典，包含了从web服务器(如Apache)提供的CGI接口中获取的值。
    
    def __call__(self, environ, start_response):
        #pdb.set_trace()
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
                                  environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        # 从请求中提取查询参数并将它们放入一个类字典对象中
        environ['params'] = { key: params.getvalue(key) for key in params }
        handler = self.pathmap.get((method,path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        return function
    
