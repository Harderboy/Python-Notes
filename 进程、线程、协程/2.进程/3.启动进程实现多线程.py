'''
multiprocessing 三方库
跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象

'''

from multiprocessing import Process
import time
import os


def run():
    while True:
        print("runrunrun")
        time.sleep(1.2)


def run2(str):
    while True:
        print("%s%s%s-%d-%d" % (str, str, str, os.getpid(), os.getppid()))
        time.sleep(1.2)


if __name__ == "__main__":
    print("主（父）进程启动-%d"%(os.getpid()))
    print(type(os.getpid()))
    # 创建子进程
    # target 说明进程执行的任务
    # p = Process(target=run)
    # 传参
    p = Process(target=run2, args=('run', ))  # 元组只有一个参数的话需要在第一个元素后面添加一个逗号
    # 启动进程
    p.start()

    while True:
        print("gogogogo-%d"%(os.getpid()))
        time.sleep(1)
