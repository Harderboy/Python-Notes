import os
import time


def copyFile(rpath, wpath):
    fr = open(rpath, "rb")
    fw = open(wpath, "wb")
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()


if __name__ == "__main__":
    path = r"F:\Github_Repo\Python_notes\进程、线程、协程\进程\file"
    toPath = r"F:\Github_Repo\Python_notes\进程、线程、协程\进程\tofile"

    # 读取path下的所有文件
    filesList = os.listdir(path)

    # 启动循环处理每一个文件
    start = time.time()
    for fileName in filesList:
        copyFile(os.path.join(path, fileName), os.path.join(toPath, fileName))

    end = time.time()
    print("总耗时为：%0.2f" % (end - start))
