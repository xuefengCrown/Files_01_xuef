
from wsgi_server import make_server

def application(environ, start_response):
    # TODO: test environ

    status = '200 OK'
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    # 调用wsgi_server提供的钩子,直接返回HTTP状态码和响应头
    start_response(status, headers)

    # 构造response body(响应正文), 并传递给 wsgi_server
    ret = [("%s: %s\n" % (key, val)).encode("utf-8")
               for key,val in environ.items()]
    return ret

if __name__ == '__main__':
    PORT = 8080
    httpd = make_server(('0.0.0.0',PORT), application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()

# WSGI
"""
1.框架提供一个可调用的’应用’（WSGI规格并没有要求如何实现）
2.服务器每次接收到HTTP客户端请求后，执行可调用的’应用’。
服务器把一个包含了WSGI/CGI变量的字典和一个可调用的’start_response’做为参数给
可调用的’application’。
3.框架/应用生成HTTP状态和HTTP响应头，然后把它们传给可调用的’start_response’，
让服务器保存它们。框架/应用也返回一个响应体。
4.服务器把状态，响应头，响应体合并到HTTP响应里，然后传给（HTTP）客户端（这步不是（WSGI）
规格里的一部分，但它是后面流程中的一步，为了解释清楚我加上了这步）
"""
