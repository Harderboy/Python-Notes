# 有序字典
from collections import OrderedDict
# 写入数据
from pyexcel_xls import save_data


def xlsExcelFileMaker(path, data):
    dict = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        dict[sheetName] = sheetValue
        dict.update(d)
    # 保存
    save_data(path, dict)


if __name__ == "__main__":
    filepath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\记分册_2班.xls"
    dict = {
        "表一": [[1, 2, 3], [3, 4, 5], [6, 7, 8]],
        "表二": [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
    }
    xlsExcelFileMaker(filepath, dict)
