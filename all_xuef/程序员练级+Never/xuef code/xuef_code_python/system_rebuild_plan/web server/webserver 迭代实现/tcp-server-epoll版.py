import select
import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsocopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('', 7788))
server.listen(5)

epoll = select.epoll()

epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLET)

connections = {}

addrs = {}

while True:
    # epoll进行fd扫描的地方--未指定超时时间则为阻塞等待    
    epoll_list = epoll.poll()

    for fd,events in epoll_list:
        # 监听套接字被激活
        if fd == s.fileno():
            client_socket,addr = s.accept()
            print("有新的客户端到来 %s" % str(addr))
            # 保存服务套接字和addr
            connections[client_socket.fileno()] = client_socket
            addrs[client_socket.fileno()] = addr

            epoll.register(client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
        elif events == select.EPOLLIN: # 可读
            recv_data = connections[fd].recv(1024)
            if len(recv_data)>0:
                print("[*] recv: %s" % recv_data)
            else:
                epoll.unregister(fd)
                connections[fd].close()
                print("%s---offline---" % str(addrs[fd]))


















































