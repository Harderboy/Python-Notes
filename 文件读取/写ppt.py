import win32com
import win32com.client


def pptFileMaker(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    # 增加一个ppt
    pptFile = ppt.Presentations.Add()

    # 创建页(一页只有两个框)
    # pptFile.Slides.Add(参数1, 参数2)：参数1为页数（第几页，从1开始），参数2为类型（ppt新建幻灯片类型）
    page1 = pptFile.Slides.Add(1, 1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "Htomato is a good man"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "lh is a good man"

    page2 = pptFile.Slides.Add(2, 1)
    t3 = page2.Shapes[0].TextFrame.TextRange
    t3.Text = "Newbie is a good man"
    t4 = page2.Shapes[1].TextFrame.TextRange
    t4.Text = "lh is a good man"

    page3 = pptFile.Slides.Add(3, 2)
    t4 = page3.Shapes[0].TextFrame.TextRange
    t4.Text = "TalkIsCheap is a good man"
    # 类型2输入标题

    # 保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()


if __name__ == "__main__":
    filepath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\ppt.ppt"
    pptFileMaker(filepath)
