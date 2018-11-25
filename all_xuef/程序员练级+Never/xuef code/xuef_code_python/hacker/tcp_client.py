
import socket 

##target_host = 'www.baidu.com'
##target_port = 80
target_host = '127.0.0.1'
target_port = 9999
# 建立一个 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接客户端
client.connect((target_host, target_port))

# 发送数据
client.send("GET / HTTP/1.1\r\nHOST: baidu.com\r\n\r\n".encode())

# 接收数据
response = client.recv(4096)

print(response)
