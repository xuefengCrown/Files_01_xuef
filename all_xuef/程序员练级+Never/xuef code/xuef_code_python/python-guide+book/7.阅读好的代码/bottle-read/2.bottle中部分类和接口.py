
"""
bottle.Bottle
    代表一个独立的wsgi应用，由一下部分组成：routes, callbacks, plugins, resources and configuration。
    
    __call__: Bottle定义了__call__函数, 使得Bottle的实例能成为一个callable。
    在前文提到，web框架（或Application）需要提供一个callbale对象给web服务器，
    bottle提供的就是Bottle实例
    
"""
def __call__(self, environ, start_response):
　　""" Each instance of :class:'Bottle' is a WSGI application. """
   return self.wsgi(environ, start_response)   


##下面是Bottle.wsgi函数的核心代码，主要调用两个比较重要的函数：_handle, _cast
def wsgi(self, environ, start_response):
    """ The bottle WSGI-interface. """
    try:
        out = self._cast(self._handle(environ))
        # rfc2616 section 4.3
        if response._status_code in (100, 101, 204, 304)\
                or environ['REQUEST_METHOD'] == 'HEAD':
            if hasattr(out, 'close'): out.close()
            out = []
        start_response(response._status_line, response.headerlist)
        return out

##_handle：处理请求，最终调用到application ，简化后的代码如下：
def _handle(self, environ):
    self.trigger_hook('before_request')
    route, args = self.router.match(environ)
    out = route.call(**args)
    self.trigger_hook('after_request')
    return out
##_cast: 标准的wsgi接口对Application的返回值要求严格，必须迭代返回字符串。
##bottle做了一些扩展，可以允许App返回更加丰富的类型，比如dict，File等。
##_cast函数对_handle函数返回值进行处理，使之符合wsgi规范。


"""
bottle.Route
    封装了路由规则与对应的回调
 
bottle.Router
    A Router is an ordered collection of route->target pairs.
    It is used to  efficiently match WSGI requests against a number of routes
    and return the first target that satisfies the request.
"""


"""
ServerAdapter
    所有bottle适配的web服务器的基类，子类只要实现run方法就可以了，bottle里面有大量的Web服务器的适配。
    下表来自官网，介绍了bottle支持的各种web服务器，以及各自的特性。
"""
##可以看到，bottle适配的web服务器很丰富。工作模式也很全面，有多线程的（如paste）、
##有多进程模式的（如gunicorn）、也有基于协程的（如gevent）。
##具体选择哪种web服务器取决于应用的特性，比如是CPU bound还是IO bound。


"""
bottle.run
    启动wsgi服务器。几个比较重要的参数
    app： wsgi application，即可以是bottle.Bottle 也开始是任何满足wsgi 接口的函数
    server： wsgi http server，字符串
    host：port： 监听端口
    
    核心逻辑：
    ServerAdapter.run(app)。
"""

##最后，bottle源码中有一些使用descriptor的例子，实现很巧妙，值得一读。























    







     








