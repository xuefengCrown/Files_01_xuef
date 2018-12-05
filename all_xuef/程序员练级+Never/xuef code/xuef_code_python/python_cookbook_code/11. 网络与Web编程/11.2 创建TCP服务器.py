
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()


#socketserver 可以让我们很容易的创建简单的TCP服务器。
#但是，你需要注意的是，默认情况下这种服务器是单线程的，一次只能为一个客户端连接服务。
#如果你想处理多个客户端，可以初始化一个 ForkingTCPServer 或者是 ThreadingTCPServer 对象。

"""
from socketserver import ThreadingTCPServer
if __name__ == '__main__':
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
"""

