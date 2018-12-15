
"""
micro web-frame

Bottle 提供了一个 Web 框架的核心功能，如：
    1. 路由，支持动态的 URL 路由
    2. 模板，内置了模板功能，同时支持 mako, jinja2 和 cheetah
    3. 表单，文件上传，cookies，headers 等的处理
    4. 支持多种 WSGI Server，如 cherrypy, eventlet, twisted 等等
关于 bottle 的使用，可以参考官方文档：https://bottlepy.org/docs/dev/index.html。
"""

# WSGI abstraction: Request and response management
# Routing
# Error handling
# Server adapter
# Templates
# Database ?

__author__ = 'xuef'
__version__ = '0.1-dev'
__license__ = 'MIT'


# import libs
import re
import cgi
from http.cookiejar import Cookie
import threading
import pdb

## parse query-string
try:
    from urlparse import parse_qs 
except ImportError:
    from cgi import parse_qs


# WSGI abstraction: Request and response management
##TODO: 处理对静态文件的请求
def WSGIHandler(environ, start_response):
    """The bottle WSGI-handler."""
    global request
    #global response
    request.bind(environ)
    #pdb.set_trace()
    #response.bind()
    try:
        handler, args = match_url(request.path, request.method)
        #pdb.set_trace()
        if not handler:
            raise HTTPError(404, "Not found")
        
        return handler(request, start_response)
    except:
        raise


#########
# Exceptions and Events
#########
class BottleException(Exception):
    """ A base class for exceptions used by bottle. """
    pass


class HTTPError(BottleException):
    """ A way to break the execution and instantly jump to an error handler. """
    def __init__(self, status, text):
        self.output = text
        self.http_status = int(status)

    def __str__(self):
        return self.output

    
class RouteError(BottleException):
    """ This is a base class for all routing related exceptions """


class RouterUnknownModeError(RouteError):
    pass


class RouteSyntaxError(RouteError):
    """ The route parser found something not supported by this router. """


class RouteBuildError(RouteError):
    """ The route could not be built. """


# Request
##封装一次HTTP 请求
class Request(threading.local): # 理解什么是一次请求，如何表示?
    """ Represents a single request using thread-local namespace. """

    def bind(self, environ):
        """ Binds the enviroment of the current request to this request handler """
        # environ 是一个字典包含了 CGI 的环境变量，
        # 更多 environ 内容参考: https://www.python.org/dev/peps/pep-3333/#id24
        self._environ = environ
        self._GET = None
        self._POST = None
        self._GETPOST = None
        self._COOKIES = None
        self.path = self._environ.get('PATH_INFO', '/').strip()
        if not self.path.startswith('/'):
            self.path = '/' + self.path
            
    @property
    def method(self):
        ''' Returns the request method (GET,POST,PUT,DELETE,...) '''
        return self._environ.get('REQUEST_METHOD', 'GET').upper()

    @property
    def query_string(self):
        ''' Content of QUERY_STRING '''
        return self._environ.get('QUERY_STRING', '')

    @property
    def content_len(self):
        ''' Content of CONTENT_LENGTH '''
        try:
            return int(self._environ.get('CONTENT_LENGTH', '0'))
        except ValueError:
            return 0

    @property
    def GET(self):
        """Returns a dict with GET parameters."""
        if self._GET is None:
            raw_dict = parse_qs(self.query_string, keep_blank_values=1)
            self._GET = {}
            for key, value in raw_dict.items():
                self._GET[key] = value[0] if len(value) == 1 else value
        
        return self._GET

    # POST 属性从 wsgi.input 中获取内容（也就是表单提交的内容）放入当前请求的变量中，
    # 可以通过 request.POST['xxx'] 来获取数据。
    # 注意以字典格式作为数据统一接口的方便性!
    @property
    def POST(self):
        """Returns a dict with parsed POST data."""
        if self._POST is None:
            raw_data = cgi.FieldStorage(fp=self._environ['wsgi.input'], environ=self._environ)
            self._POST = {}
            if raw_data:
                for key in raw_data:
                    if isinstance(raw_data[key], list):
                        self._POST[key] = [v.value for v in raw_data[key]]
                    elif raw_data[key].filename:
                        self._POST[key] = raw_data[key]
                    else:
                        self._POST[key] = raw_data[key].value
        return self._POST

    @property
    def params(self):
        ''' Returns a mix of GET and POST data. POST overwrites GET '''
        if self._GETPOST is None:
            self._GETPOST = dict(self.GET)
            self._GETPOST.update(dict(self.POST))
        return self._GETPOST

    @property
    def COOKIES(self):
        """Returns a dict with COOKIES."""
        if self._COOKIES is None:
            raw_dict = Cookie.SimpleCookie(self._environ.get('HTTP_COOKIE',''))
            self._COOKIES = {}
            for cookie in raw_dict.values():
                self._COOKIES[cookie.key] = cookie.value
        return self._COOKIES



# Routing
def add_route(route, handler, method='GET', simple=False):
    """ Adds a new route to the route mappings.

        Example:
        def hello():
          return "Hello world!"
        add_route(r'/hello', hello)"""
    method = method.strip().upper()
    #pdb.set_trace()
    if re.match(r'^/(\w+/)*\w*$', route) or simple:
        #>>> d.setdefault('get', {})['/hello']='hello'
        #>>> d
        #{'get': {'/hello': 'hello'}}
        ROUTES_SIMPLE.setdefault(method, {})[route] = handler
        
    else:
        raise("目前只支持简单route")
        # route = compile_route(route)
        # ROUTES_REGEXP.setdefault(method, []).append([route, handler])
        
def route(url, **kargs):
    def wrapper(handler):
        add_route(url, handler, **kargs)
        print("  [*] add route--> ", url, ":", handler)
        return handler   
    return wrapper


def match_url(url, method='GET'):
    """Returns the first matching handler and a parameter dict or (None, None).
    
    This reorders the ROUTING_REGEXP list every 1000 requests.
    To turn this off, use OPTIMIZER=False"""
    url = '/' + url.strip().lstrip("/")
    # Search for static routes first
    route = ROUTES_SIMPLE.get(method,{}).get(url,None)
    if route:
        return (route, {})
    
    # Now search regexp routes
    # TODO
    return (None, None)


# Server adapter(这里的Adapter模式值得学习)

class ServerAdapter(object):
    def __init__(self, host='127.0.0.1', port=8080, **kargs):
        self.host = host
        self.port = int(port)
        self.options = kargs

    def __repr__(self):
        return "%s (%s:%d)" % (self.__class__.__name__, self.host, self.port)

    def run(self, handler):
        print("[*] Server Listening on port: {port}".format(port = self.port))
        pass


## 目前只支持Python内置server: wsgiref.simple_server
class WSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server
        super().run(handler)
        srv = make_server(self.host, self.port, handler)
        srv.serve_forever()



# 启动app
## 我们应该允许用户指定server类型(当然首先要与我们的框架兼容)
## 允许指定 host/port，以及其他配置参数
def run(server=WSGIRefServer, host='127.0.0.1', port=8080, optinmize = False, **kargs):
    """ Runs bottle as a web server, using Python's built-in wsgiref implementation by default.
    
    You may choose between WSGIRefServer, CherryPyServer, FlupServer and
    PasteServer or write your own server adapter.
    """
    # Instanciate server, if it is a class instead of an instance
    if isinstance(server, type) and issubclass(server, ServerAdapter):
        server = server(host=host, port=port, **kargs)

    if not isinstance(server, ServerAdapter):
        raise RuntimeError("Server must be a subclass of ServerAdapter")
    
    try:
        server.run(WSGIHandler)
    except KeyboardInterrupt:
        print("Shuting down...")

        
# Module initialization

ROUTES_SIMPLE = {}

##TEMPLATE_PATH = ['./%s.tpl', './views/%s.tpl']
##TEMPLATES = {}

request = Request()





