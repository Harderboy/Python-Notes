import threading
import time


def func():
    # 事件对象
    event = threading.Event()

    def run():
        for i in range(5):
            # 阻塞，等待事件的触发
            event.wait()
            # 重置
            # event.clear()
            print("sunck is good man%d" % i)
    threading.Thread(target=run).start()
    # t = threading.Thread(target=run).start()
    # print(t)
    # print(type(t))
    return event


e = func()

# 触发事件（任何地方都可触发，只要知道事件对象）
for i in range(5):
    time.sleep(2)
    e.set()
