import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '10.198.115.36'
port = 8900
addr = (host, port)

while True:
    data = input("请输入数据：")
    client.sendto(data.encode("utf-8"), addr)
    info, addr1 = client.recvfrom(1024)
    print("服务器说：" + info.decode("utf-8"))
