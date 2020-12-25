from multiprocessing import Process, Queue
import os
import time


def write(q):
    print("启动写子进程%d" % (os.getpid()))
    for chr in ["A", "B", "C"]:
        q.put(chr)
        time.sleep(1)
    print("结束写子进程%d" % (os.getpid()))


def read(q):
    print("启动读子进程%d" % (os.getpid()))
    while True:
        value = q.get(True)
        print("value = " + value)
    print("结束读子进程%d" % (os.getpid()))


if __name__ == "__main__":
    # 父进程创建队列，并传递给子进程
    q = Queue()

    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    pw.start()
    pr.start()

    # 先停止写进程，再停止读进程
    pw.join()
    # pr 进程里是个死循环，无法等待期结束，只能强制结束
    pr.terminate()

    # while True:
    #     pass
    print("父进程结束")
