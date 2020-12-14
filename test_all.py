import random

list1 = [20, 16, 10, 5]
random.shuffle(list1)
print("随机排序列表:", list1)

random.shuffle(list1)
print("随机排序列表:", list1)

'''
5=101
7=111
------
2=010
'''
# 5^7=2
print(5 ^ 7)


num1 = 12
num2 = 10
if num1 and num2:
    print("****")

print(num1, num2)

# -6
# 计算机普遍使用补码表示负数
print(~5)
# 原码 00000101
# 执行~11111010（负数）
# 反码 10000101
# 补码 10000110 （-6）


print('tom is a "good" man')
print("tom is a 'good'man")
print("tom is a \"good\" man")
print("tom is a \'good\' man")
print('tom is a \"good\" man')

str1 = "sunk is a good man"
print("str1 = {}".format(str1.upper()))
print("str1 = {}".format(str1.title()))
# 字符串居中
print("str1 = {}".format(str1.center(30, "*")))
# 字符串左对齐 ljust(width[, fillchar]) fillchar默认空格
print("str1 = {}".format(str1.ljust(30, "*")))

num3 = 10
while num3 >= 5:
    print(num3)
    num3 -= 1

str2 = "sunk is a good man"
index = 0
while index < len(str1):
    print("str[{0}] = {1}".format(index, str1[index]))
    index += 1

"""
str3 = range(100, 1000)
for i in str3:
"""
# 改进
n = 0
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a**3+b**3+c**3 == i:
        print(i)
        n += 1

print(n)

range1 = range(0, 5)
print(type(range1))
print(range1)
print(list(range1))


# num = int(input())

print(" " != " ")


dict = {}
dict['name'] = 'liu'
dict['age'] = 6
print(dict)



s1 = set([1, 2, 3, 5, 4, 2, 3])
s1.add((1, 12, 3))
print(s1)

s2 = set((1, 2, 2, 3, 5))
print(s2)
s3 = set({1: 'name', 2: 'age'})
print(s3)


import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}
data2 = (1,3,'good')

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data2, output)

output.close()

# 使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
print(data1)

pkl_file.close()


# -*- coding: utf-8 -*-
import time

# print(time.time())

t = time.time()
t1 =time.gmtime(t)
print(t1)

t2 = time.localtime(t)
print(t2)

t3 = time.mktime(t2)
print(t3)

t4 = time.asctime(t2)
print(t4)

t5 = time.ctime(t)
print(t5)

t6 = time.strftime("%Y-%m-%d %H:%M:%S")
print(t6)

# 将时间元组转换为指定格式的字符串，参数2为时间元组，如果没有参数2，默认为当前时间
t6 = time.strftime("%Y-%m-%d %X", t2)
print(t6)
print(type(t6))


# 将时间字符串转换为时间元组

t7 = time.strptime(t6, '%Y-%m-%d %X')
print(t7)
print(type(t7))



import time

t = time.clock()
# print(t)
sum = 0
for i in range(10000000):
    sum += i
print(sum)
print(time.clock())


class Person(object):
    # 定义属性
    name = "lihua"
    age = 0
    # 定义方法
    def run(self):
        print("run")


'''
实例化对象
格式：对象名 = 类名（参数列表）
注意：类名没有参数，小括号不能省略
'''
per1 = Person()
print(per1)
print(type(per1))

per2 = Person()
print(per2)
print(type(per2))

import os
os.system('notepad')

class Person(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Person(self.num + other.num)
    # 运算符重载
    def __str__(self):
        return "num = " + str(self.num)

per1 = Person(1)
per2 = Person(2)

print(per1 + per2)
# per1 + per2相当于per1.__add__(per2)
print(per1.__add__(per2))
print(per1)
print(per2)




import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "liuhengcsc@163.com"  # 用户名
mail_pass = "OLWYNABMRCWCBGEM"  # 口令

sender = 'liuhengcsc@163.com'
receivers = ['1324631884@qq.com', 'liuhengcsc@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = sender
# message['To'] = receivers

subject = 'hello world!'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
