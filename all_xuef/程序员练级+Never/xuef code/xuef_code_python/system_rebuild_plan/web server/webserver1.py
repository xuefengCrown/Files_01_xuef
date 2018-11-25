
import socket

HOST, PORT = '0.0.0.0', 8080
def server_start():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ???
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    # 可建立socket连接的最大个数
    server_socket.listen(1)
    print('Serving HTTP on port %s ...' % PORT)
    while 1:
        client_socket, client_addr = server_socket.accept()
        req = client_socket.recv(1024)
        print("[*] %s: %s" % (client_addr, req))

        # """HTTP/1.1 200 OK\r\n Content-Type:text/html\r\n\r\nWelcome!"""
        http_response = """HTTP/1.1 200 OK\r\n\r\nWelcome!"""
        client_socket.send(http_response.encode())
        client_socket.close()
if __name__ == '-_main__':
    server_start()

# TODO
"""
有一个问题: 怎样在你的刚完成的WEB服务器下运行 Django 应用、Flask 应用和 Pyramid  应用？
在不单独修改服务器来适应这些不同的 WEB 框架的情况下。
"""
