import win32com
import win32com.client
import time


def wordFileReader(path):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc = mw.Documents.Open(path)
    # time.sleep(1)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)

    # 关闭文件
    doc.Close()
    # 退出word
    mw.Quit()


if __name__ == "__main__":
    path = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\doc.docx"
    wordFileReader(path)