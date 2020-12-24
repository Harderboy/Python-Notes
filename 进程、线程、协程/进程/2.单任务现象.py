import time


def run():
    while True:
        print("runrunrun")
        time.sleep(1.2)


if __name__ == "__main__":
    while True:
        print("gogogogo")
        time.sleep(1)
    # 不会执行run方法，只有上面的while循环结束后才可以执行
    run()
