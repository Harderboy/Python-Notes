import win32com
import win32com.client
import time


def wordFileReader(srcPath, desPath):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc = mw.Documents.Open(srcPath)

    # 将word的数据保存到另一个文件
    doc.SaveAs(desPath, 2)  # 2表示为txt文件

    # 关闭文件
    doc.Close()
    # 退出word
    mw.Quit()


if __name__ == "__main__":
    srcPath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\doc.docx"
    desPath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\doc.txt"
    wordFileReader(srcPath, desPath)