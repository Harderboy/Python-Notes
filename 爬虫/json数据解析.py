"""
概念：一种保存数据的格式，是一种字符串
作用：可以保存本地的json文件，也可以将json字符串进行传输，通常将json称为轻量级的传输方式
组成：
    {}：代表对象（字典）
    []：代表列表
    :   代表键值对
    ,   分割两个部分
    ""  JSON中，标准语法中，不支持单引号，属性或者属性值，都必须是双引号括起来的

要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
"""

import json

jsonStr = '{"url": "http://www.runoob.com", "no": 1, "name": "Runoob"}'
print(type(json))

# 将json格式的字符串转换为python数据类型的对象
jsonData = json.loads(jsonStr)
# print(jsonData)
print(type(jsonData))
# print(jsonData["url"])

# 将python数据类型的对象转为json格式的字符串

jsonData2 = {'url': 'http://www.runoob.com', 'no': 1, 'name': 'Runoob'}
jsonStr2 = json.dumps(jsonData2)
# print(jsonStr2)
print(type(jsonStr2))

# 读取本地json文件：json.load(f)，load不加s代表读文件

path1 = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\json.json"
with open(path1, "rb") as f:
    data = json.load(f)
    # print(data)
    # 字典类型
    print(type(data))

# 写本地json文件，json.dump(f)，dump不加s代表写文件

path2 = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\json2.json"
jsonData3 = {'url': 'http://www.runoob.com', 'no': 1, 'name': 'Runoob'}
with open(path2, "w") as f:
    json.dump(jsonData3, f)
