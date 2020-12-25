import socket
import threading

# 创建一个socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP端口
server.bind(('10.198.112.111', 8080))
# 监听
server.listen(5)


def run(ck):
    # 没有用到ck变量
    data = clientSocket.recv(1024)
    print("收到" + str(clientSocket) + "的数据" + data.decode("utf-8"))
    # sendData = input("请输入返回给客户端的数据")
    clientSocket.send("sunck is good man".encode("utf-8"))


print("服务器启动成功，等待客户端链接")
while True:
    # 等待连接
    clientSocket, clientAddress = server.accept()
    print("%s -- %s 连接成功" % (str(clientSocket), clientAddress))
    t = threading.Thread(target=run, args=(clientSocket,))

    t.start()

# while True:
#     # 等待客户端连接
#     clientSocket, clientAddress = server.accept()
#     # 启动有一个线程，将当前连接clientSocket交给线程
