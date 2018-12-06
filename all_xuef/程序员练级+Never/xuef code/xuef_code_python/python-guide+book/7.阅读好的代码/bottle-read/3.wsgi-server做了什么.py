
"""
wsgi服务器做了什么?
1. 监听HTTP服务端口(TCPServer,默认80 port)
2. 接收HTTP请求并解析封装成 environ 环境字典
3. 负责调用应用程序，将environment和 start_response方法传入(服务器提供给app的钩子用于插入响应头)
4. 将 app响应的正文封装成HTTP响应报文返回给客户端
"""


