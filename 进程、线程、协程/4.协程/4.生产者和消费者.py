def producer(c):
    c.send(None)  # 先用空值启动生成器，因为开始没有变量接受yield表达式
    for i in range(5):
        print('生产者产生了数据 %d' % i)
        r = c.send(str(i))  # 启动后再传入真实的值
        # 这里使用str(i)的原因在于，i为int且i=0时，c.send(i)给消费者函数中n赋值，n为0时函数会退出，抛出StopIteration
        print('消费者返回 %s' % r)
    c.close()


def consumer():
    data = ''
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了 %s" % n)
        data = '200'


# 返回值是一个生成器
c = consumer()
producer(c)