
import socket
import threading

# 客户端处理线程
def handle_client(new_socket):
    #while True:
        req = new_socket.recv(1024)
        #if not req: break
        print("[*] Received %s" % req)
        new_socket.send("Ack".encode('utf-8'))

def main():
    bind_ip, bind_port = '0.0.0.0', 9999
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((bind_ip, bind_port))
    server_socket.listen(5)
    print("[*] Listening on %s:%d" % (bind_ip, bind_port))
    while True:
        new_socket, addr = server_socket.accept()
        print("[*] Accept connection from %s:%d" % (addr[0], addr[1]))
        # 启动一个线程来服务客户端
        thd = threading.Thread(target=handle_client, args=(new_socket,))
        thd.start()
if __name__ == '__main__':
    main()
