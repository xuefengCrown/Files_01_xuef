""" 一个简单的TCP代理 (python3.6) """
import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host,local_port))
    except:
        print("[!!] Failed to listen on %s:%d" % (local_host,local_port))
        print("[!!] Check for other listening sockets or correct permissions.")
        sys.exit(0)
    print("[*] Listening on %s:%d" % (local_host,local_port))
    server.listen(5)
    while True:
        client_socket, addr = server.accept()
        # print out the local connection information
        print("[==>] Received incoming connection from %s:%d" % (addr[0],addr[1]))
        # start a thread to talk to the remote host
        proxy_thread = threading.Thread(target=proxy_handler,\
                                        args=(client_socket,remote_host,remote_port,receive_first))
        proxy_thread.start()

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    # 连接远程服务器(目标服务器)connect to the remote host
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host,remote_port))
    # 先从远程服务器接收数据 receive data from the remote end if necessary
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        ## 转储(响应)数据包中数据，查看是否有感兴趣的内容
        hexdump(remote_buffer)

        # send it to our response handler(消息处理器???)
        ## 在此函数中，我们可以修改数据包的内容，进行模糊测试任务，
        ## 检测认证问题，或者其他任何你想做的事情。
        remote_buffer = response_handler(remote_buffer)
        # if we have data to send to our local client, send it
        if len(remote_buffer):
            print("[<==] Sending %d bytes to localhost." % len(remote_buffer))
            client_socket.send(remote_buffer)
    while True:
        # read from local host
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            print("[==>] Received %d bytes from localhost." % len(local_buffer))
            ## ## 转储(请求)数据包中数据，查看是否有感兴趣的内容
            hexdump(local_buffer)
            # send it to our request handler
            local_buffer = request_handler(local_buffer)
            # send off the data to the remote host
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")
        # 接收远程服务器的响应并发送给客户端 receive back the response
        remote_buffer = receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Received %d bytes from remote." % len(remote_buffer))
            ## ## 转储(响应)数据包中数据，查看是否有感兴趣的内容
            hexdump(remote_buffer)
            # send to our response handler
            remote_buffer = response_handler(remote_buffer)
            # send the response to the local socket
            client_socket.send(remote_buffer)
            print("[<==] Sent to localhost.")
            
        # if no more data on either side, close the connections
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break

# this is a pretty hex dumping function directly taken from the comments here:
# http://code.activestate.com/recipes/142812-hex-dumper/
def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, str) else 2
    for i in range(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append( b"%04X %-*s %s" % (i, length*(digits + 1), hexa, text))
    print(b'\n'.join(result))

def receive_from(connection):
    buffer = ""
    # We set a 2 second timeout; depending on your target, this may need to be adjusted
    connection.settimeout(5)
    try:
        # keep reading into the buffer until there's no more data or we time out
        while True:
            data = connection.recv(4096)
            if not data: break
            buffer += data
    except:
        pass
    return buffer

# modify any requests destined for the remote host
def request_handler(buffer):
    # perform packet modifications
    return buffer

# modify any responses destined for the local host
def response_handler(buffer):
    # perform packet modifications
    return buffer
"""
读入命令行参数，然后运行服务端(代理服务器)的循环以监听客户端的连接请求。
当一个新的请求到达时，我们将它交给 proxy_handler 函数处理，
此函数接收每一个比特的数据，然后发送到目标远程主机。
"""
def main():
    # no fancy command-line parsing here
    if len(sys.argv[1:]) != 5:
        print("Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)
    # setup local listening parameters
    local_host, local_port = sys.argv[1], int(sys.argv[2])
    # setup remote target
    remote_host, remote_port = sys.argv[3], int(sys.argv[4])
    # this tells our proxy to connect and receive data
    # before sending to the remote host
    receive_first = True if "True" in sys.argv[5] else False
    # now spin up(起转) our listening socket
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)

# python tcp_proxy.py 127.0.0.1 9999 183.232.231.172 80 True
if __name__ == '__main__':
    main()















