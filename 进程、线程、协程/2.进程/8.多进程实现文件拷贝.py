import os
import time
from multiprocessing import Pool


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

    start = time.time()
    pp = Pool()
    # 启动循环处理每一个文件
    for fileName in filesList:
        pp.apply_async(copyFile,
                       args=(os.path.join(path, fileName),
                             os.path.join(path, fileName)))
    pp.close()
    pp.join()
    end = time.time()
    print("总耗时为：%0.2f" % (end - start))
    # 创建进程比较耗费时间，需比较创建进程和复制文件时间的代价（数量级比较）
