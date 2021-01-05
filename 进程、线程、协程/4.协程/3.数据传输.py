def run():
    # 空变量，存储的作用，data始终为空
    data = ''
    r = yield data  # 程序第一次调用
    print(1, r, data)
    r = yield data
    print(2, r, data)
    r = yield data
    print(3, r, data)
    r = yield data


# 返回值是一个生成器
m = run()
# 启动m
print(m.send(None))
# 使用 send(params) 不断传入值，传给r
print(m.send("a"))
print(m.send("b"))
print(m.send(2))
'''
参考链接：
    Python生成器及send用法讲解：https://www.cnblogs.com/Gaoqiking/p/10577309.html
    python-生成器及send()用法：http://www.mamicode.com/info-detail-2399245.html
    Python 生成器与它的 send，throw，close 方法：https://blog.csdn.net/jpch89/article/details/87036970
    Python生成器及send用法讲解：https://www.cnblogs.com/nymrli/p/9416949.html
'''
