import win32com
import win32com.client
import os
import time


def wordFileMaker(path, filename):
    word = win32com.client.Dispatch("Word.Application")

    # 让文件可见
    word.Visible = True

    # 创建文档
    doc = word.Documents.Add()
    # 写内容
    # 从头写
    r = doc.Range(0, 0)
    r.InsertAfter("亲爱的" + filename + "\n")
    r.InsertAfter("      我想你...." + "\n")

    # 存储文件
    doc.SaveAs(path)
    # 关闭文件
    doc.Close()
    # 退出word
    word.Quit()


if __name__ == "__main__":
    names = ["张三", "李四", "王五"]
    for name in names:
        path = os.path.join(os.getcwd(), name)
        # print(path)
        wordFileMaker(path, name)
        time.sleep(1)
