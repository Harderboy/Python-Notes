# -*- coding: UTF-8 -*-
import urllib.request

url = "http://www.baidu.com"

# 解码
newUrl = urllib.request.unquote(url)
print(newUrl)

# 编码
newUrl2 = urllib.request.quote(newUrl)
print(newUrl2)

# 向指定的url地址发送请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen(newUrl)

# 读取文件的全部内容，返回的为字符串
data = response.read()
# print(data)
print(type(data))

data2 = response.read().decode("utf-8")
# print(data2)
print(type(data2))

# 读取一行
# data = response.readline()

# 读取文件的全部内容，会把读取到的数据赋值给一个列表变量
'''
data = response.readlines()
print(data)
print(type(data))
print(len(data))
'''

# with open(r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\file\file1.html", "wb") as f:
#    f.write(data)

# 返回当前环境的有关信息
print(response.info())

# 返回状态码
# print(response.getcode())
# if response.getcode() == 200 or response.getcode() == 304:
# 处理
#    pass

# 返回当前正在爬取的url地址
print(response.geturl())
