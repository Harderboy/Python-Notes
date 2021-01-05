import threading
import queue
import random
import time


# 生产者
def producer(id, q):
    while True:
        num = random.randint(0, 10000)
        q.put(num)
        print("生产者%d生产了%d数据放入了队列" % (id, num))
        time.sleep(3)
    # 任务完成
    q.task_done()


# 消费者
def consumer(id, q):
    while True:
        item = q.get()
        if item is None:
            break
        print("消费者%d消费了%d数据" % (id, item))


if __name__ == "__main__":
    # 消息队列
    q = queue.Queue()

    # 启动生产者
    for i in range(4):
        threading.Thread(target=producer, args=(i, q)).start()
    # 启动消费者
    for i in range(3):
        threading.Thread(target=consumer, args=(i, q)).start()
