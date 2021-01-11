# coding=utf-8
'''
美国制定了一套字符编码，对英语字符与二进制位之间的关系，做了统一规定。这被称为 ASCII 码
ASCII 码使用指定的7 位或8 位二进制数组合来表示128 或256 种可能的字符

Python3中的chr()不仅仅支持ASCII码的转换，而且直接支持了更为适用的Unicode码的转换，但是Unicode码的0-127和ASCII码还是一样的，所以不用担心ASCII不能用的问题。

UTF-8 就是在互联网上使用最广的一种 Unicode 的实现方式。

chr() 用一个整数作参数，返回一个对应的字符。
chr(i) i -- 可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)
返回值是当前整数对应的 ASCII 字符（Unicode字符）。

'''
# 用户输入ASCII码值（Unicode码）
n = int(input("请输入一个数字（ASCII码值）："))
print("ASCII码值%d对应的字符为：%s" % (n, chr(n)))

'''
对英语字符与二进制位之间的关系，做了统一规定。这被称为 ASCII 码

ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。

返回值是对应的十进制整数。
'''
# 用户输入字符
c = input("请输入一个字符：")
print("%s对应的ASCII码值为：%d" % (c, ord(c)))
