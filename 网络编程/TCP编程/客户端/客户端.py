'''
客户端：创建TCP连接时，主动发起的连接的为客户端
服务器端：接收客户端连接
'''

import socket

# 1.创建一个socket
# 参数1：指定协议 AF_INET 或者 AF_INET6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.建立连接
# 参数：是一个元组，第一个元素为要连接服务器的IP地址，第二个元素为端口号

sk.connect(("www.sina.com.cn", 80))

sk.send(
    b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 等待接收数据
data = []
while True:
    # 每次接受1K的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode("utf-8")

# 断开连接
sk.close()
print(dataStr)
