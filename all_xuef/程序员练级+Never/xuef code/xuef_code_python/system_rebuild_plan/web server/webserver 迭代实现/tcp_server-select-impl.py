"""
IO多路复用???
"""
import socket
import select
import sys

def main():
    host, port = '', 8888
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("[*] Server listening on %s: %s" % (host, port))

    inputs = [server_socket, sys.stdin]
    running = True
    while True:
        # select 存在套接字上限; 而且是轮询机制
        readable, writeable, exceptional = select.select(inputs, [],[])

        for s in readable:
            if s == server_socket: #server_socket有数据到达意味着有新连接到达
                client_socket, client_addr = s.accept()
                inputs.append(client_socket)
            elif s == sys.stdin: # 键盘有数据到达
                cmd = sys.stdin.readline()
                running = False
                break
            else: # client_socket有数据到达
                data = s.recv(1024)
                if data:
                    s.send(data.encode())
                else:
                    inputs.remove(sock)
                    sock.close()
        # 如果检测到用户输入敲击键盘，那么就退出
        if not running:
            break

    server.close()     


