import socket

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP端口
server.bind(('192.168.1.7', 8080))
# 监听
server.listen(5)
print("服务区启动成功....")

# 等待连接
clientSocket, clientAddress = server.accept()

print("%s -- %s 连接成功" % (str(clientSocket), clientAddress))

while True:
    data = clientSocket.recv(1024)
    print("收到" + str(clientSocket) + "的数据" + data.decode("utf-8"))
    sendData = input("请输入返回给客户端的数据")
    clientSocket.send(sendData.encode("utf-8"))

# while True:
#     # 等待客户端连接
#     clientSocket, clientAddress = server.accept()
#     # 启动有一个线程，将当前连接clientSocket交给线程
