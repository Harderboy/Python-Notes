import csv


def csvReader(path):
    infoList = list()
    with open(path, 'r') as f:
        allFileInfo = csv.reader(f)
        # print(type(allFileInfo))
        for row in allFileInfo:
            infoList.append(row)
            # print(row)
    return infoList


if __name__ == "__main__":
    path = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\002566.csv"
    info = csvReader(path)
    print(info)
