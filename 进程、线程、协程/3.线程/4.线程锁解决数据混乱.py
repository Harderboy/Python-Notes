'''
两个线程同时工作，一个存钱，一个取钱

可能导致数据异常

思路：加锁

'''

import threading

num = 0

# 锁对象
lock = threading.Lock()


def run(n):
    global num
    # 锁（在这上或者在循环中上皆可）
    for i in range(10000000):
        # 上锁
        # 确保了这段代码只能由一个线程从头到位的完整执行
        # 阻止了多线程的并发执行，包含锁的某段代码只能以单线程模式执行，所以效率大大降低了
        # 由于可以存在多个锁，不同线程持有不同的锁，并试图获取其他的锁，可能造成死锁，导致多个线程挂起，只能靠操作系统强制终止
        # lock.acquire()
        # try:
        #     num = num + n
        #     num = num - n
        # except:
        #     print("出错了")
        # finally:
        #     # 修改完一定要释放锁
        #     lock.release()

        # 与上面代码功能相同，with lock 可以自动上锁和解锁
        with lock:
            num = num + n
            num = num - n


if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=(6, ))
    t2 = threading.Thread(target=run, args=(9, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("num= ", num)
