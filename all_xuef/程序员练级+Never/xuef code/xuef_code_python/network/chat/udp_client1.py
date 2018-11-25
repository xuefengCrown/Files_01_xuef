
import socket

def main():
    target_host = '127.0.0.1'
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((target_host, 8888))

    while 1:
        msg = input("msg2send: ")
        client.sendto(msg.encode('utf-8'), (target_host, target_port))
        # 接收数据
        data, addr = client.recvfrom(4096)
        print(addr, '>> ', data.decode('utf-8'))
        
if __name__ == '__main__':
    main()
