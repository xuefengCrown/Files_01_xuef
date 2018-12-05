
import socket
import io
import sys
import pdb
import time

# TODO
"""
有一个问题: 怎样在你的刚完成的WEB服务器下运行 Django 应用、Flask 应用和 Pyramid  应用？
在不单独修改服务器来适应这些不同的 WEB 框架的情况下。
"""
# WSGI
# WSGI提供了Python Web服务器和Python Web框架之间的一个最小接口。
# 它非常简单，在服务器和框架端都可以轻易实现。
class WSGIServer(object):
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1
    def __init__(self, server_address):
        # create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
            )
        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        
        self.server_name = socket.getfqdn(host)
        print("server-name: %s,\n hostname: %s \n" % (self.server_name, host))
        ## getfqdn() will return the fully qualified domain name
        self.server_port = port
        
        # Return headers set by Web framework/Web application
        self.headers_set = []
    def set_app(self, application):
        self.application = application
    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connection, client_address = listen_socket.accept()
            self.handle_one_request()
            
    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024)
        print(''.join(
            '< {line}\n'.format(line=line)
                for line in request_data.splitlines()
        ))
        self.parse_request(request_data)

        env = self.get_environ()

        # It's time to call our application callable and get
        # back a result that will become HTTP response body
        result = self.application(env, self.start_response)
        
        # Construct a response and send it back to the client
        self.finish_response(result)
        
    def parse_request(self, text):
        #pdb.set_trace()
        lines = text.splitlines()
        if len(lines) > 0:
            request_line = lines[0]
            request_line = request_line.rstrip(b'\r\n')
            # Break down the request line into components
            (self.request_method,  # GET
             self.path,            # /hello
             self.request_version  # HTTP/1.1
             ) = request_line.split()
        
    def get_environ(self):
        env = {}
        # The following code snippet does not follow PEP8 conventions
        # but it's formatted the way it is for demonstration purposes
        # to emphasize the required variables and their values
        #
        # Required WSGI variables
        # Web框架使用字典里的信息来决定使用哪个视图，基于指定的路由，请求方法等，
        # 从哪里读请求体，错误写到哪里去，如果有的话。
        env['wsgi.version']      = (1, 0)
        env['wsgi.url_scheme']   = 'http'
        #pdb.set_trace()
        env['wsgi.input']        = io.StringIO(str(self.request_data, encoding="utf-8"))
        env['wsgi.errors']       = sys.stderr
        env['wsgi.multithread']  = False
        env['wsgi.multiprocess'] = False
        env['wsgi.run_once']     = False
        # Required CGI variables
        env['REQUEST_METHOD']    = self.request_method    # GET
        env['PATH_INFO']         = self.path              # /hello
        env['SERVER_NAME']       = self.server_name       # localhost
        env['SERVER_PORT']       = str(self.server_port)  # 8888
        return env
    def start_response(self, status, response_headers, exc_info=None):
        # Add necessary server headers
        server_headers = [
            ('Date', time.ctime(time.time())),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]
        # To adhere to WSGI specification the start_response must return
        # a 'write' callable. We simplicity's sake we'll ignore that detail
        # for now.
        # return self.finish_response
 
    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'

            for data in result:
                response += str(data, encoding='utf-8')
            # Print formatted response data a la 'curl -v'
            print(''.join(
                '> {line}\n'.format(line=line)
                for line in response.splitlines()
            ))
            self.client_connection.sendall(response.encode('utf-8'))
        finally:
            self.client_connection.close()

#SERVER_ADDRESS = (HOST, PORT) = '', 8888
def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    # 如果一个模块经常变化就可以使用 __import__() 来动态载入。
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()



"""
首先，服务器启动并加载一个由Web框架/应用提供的可调用的’application’

然后，服务器读取请求

然后，服务器解析它

然后，服务器使用请求的数据创建了一个’environ’字典

然后，服务器使用’environ’字典和’start_response’做为参数调用’application’，
并拿到返回的响应体。

然后，服务器使用调用’application’返回的数据，由’start_response’设置的状态和响应头，
来构造HTTP响应。

最终，服务器把HTTP响应传回给户端。 
"""

##现在你有了一个可工作的WSGI服务器，它可以处理使用像Django，Flask，Pyramid或者
##你自己的WSGI框架这样的兼容WSGI的Web框架写的基本的Web应用。
##最优秀的地方是，服务器可以在不修改代码的情况下，使用不同的Web框架。


# TODO 该怎么做才能让服务器同一时间处理多个请求呢？    








































