
"""
监听套接字负责等待新的客户端进行连接
accept产生的新的套接字用来为客户端服务
"""
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(128)
server_socket, client_addr = server.accept() # 客户端连接前会阻塞

req = server_socket.recv(4096) # 等待客户端发送数据,数据到达或者客户端断开连接时解阻塞
server_socket.send("ok".encode('utf-8'))

server.close()
server_socket.close()







