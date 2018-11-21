
import socket 

target_host = '127.0.0.1'
target_port = 80

# 建立一个 socket 对象
## socket.AF_INET 声明IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 发送数据
client.sendto("hello,xuef".encode('utf-8'), (target_host, target_port))

# 接收数据
data, addr = client.recvfrom(4096)

print(data, "from ip: ", arrr)
