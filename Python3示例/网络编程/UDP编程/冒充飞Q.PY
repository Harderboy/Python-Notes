"""
TCP：建立可靠连接，三次握手，通信双方以流的形式发送数据
UDP：无需建立连接，只需拿到对方IP和端口号就可直接发送数据，不保证到达。

UDP虽然传输数据不可靠，但速度快，可靠性要求不高的可以用
"""
# 以下代码有问题

import socket
import time

str = ""  # 符合规定格式的字符串
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect(("10.198.115.36", 2425))
# udp.send(str.encode("gbk"))

while True:
    udp.send(str.encode("gbk"))
    time.sleep(1)
