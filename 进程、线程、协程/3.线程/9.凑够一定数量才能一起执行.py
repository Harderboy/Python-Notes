import threading
import time


bar = threading.Barrier(3)


def run():
    print("%s--start" % (threading.current_thread().name))
    time.sleep(2)
    # 凑够一定数量的线程才能执行，否则就一直等待
    bar.wait()
    print("%s--end" % (threading.current_thread().name))


if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()
