
import socket
import threading

def sendmsg(client, target_host, target_port):
    while 1:
        msg = input("msg2send: ")
        client.sendto(msg.encode('utf-8'), (target_host, target_port))

def recvmsg(client):
    # 接收数据
    while 1:
        data = client.recvfrom(1024)
        print(data)
def main():
    target_host = '192.168.1.110'#'127.0.0.1'
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind((target_host, 9998))

    send_thread = threading.Thread(target=sendmsg, args=(client, target_host, target_port))
    #recv_thread = threading.Thread(target=recvmsg, args=(client,))

    #recv_thread.start()
    send_thread.start()
    
    recvmsg(client)


if __name__ == '__main__':
    main()
