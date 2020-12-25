from multiprocessing import Process
import time
import os


def run():
    while True:
        print("runrunrun")
        time.sleep(1.2)


def run2(str):
    print("子进程启动")
    time.sleep(3)
    print("子进程结束")


if __name__ == "__main__":
    print("主（父）进程启动")
    # 创建子进程，并传参
    p = Process(target=run2, args=('run', ))  # 元组只有一个参数的话需要在第一个元素后面添加一个逗号
    # 启动进程
    p.start()

    # 父进程先结束，子进程后结束
    # 父进程的结束不影响子进程
    # print("父进程结束")

    # 让父进程等待子进程结束后再执行结束父进程
    p.join()
    print("父进程结束")
