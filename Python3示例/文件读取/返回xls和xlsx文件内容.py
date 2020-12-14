# 有序字典
from collections import OrderedDict
# 读取数据
from pyexcel_xls import get_data


def xlsxAndXlsFileReader(path):
    dict = OrderedDict()

    # 抓取数据
    xdata = get_data(path)

    for sheet in xdata:
        dict[sheet] = xdata[sheet]
    return dict


if __name__ == "__main__":
    filepath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\记分册_1班.xlsx"
    dict = xlsxAndXlsFileReader(filepath)
    print(dict)
    # print(dict["记分册"])
    # print(len(dict))