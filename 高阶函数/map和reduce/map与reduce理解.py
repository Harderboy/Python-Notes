# Google 文章
# 大数据相关

# python 内置了map()和reduce()函数
'''
map() 函数语法：
    map(function, iterable, ...)

参数:
    function -- 函数
    iterable -- 一个或多个序列

返回值:
    Python 2.x 返回列表。
    Python 3.x 返回迭代器。

功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回
'''

from functools import reduce


# 将单个字符转成对应的字面量整数
def charToInt(chr):
    return {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }[chr]


list1 = ["2", "1", "6", "5"]

res = map(charToInt, list1)
print(res)
print(list(res))

# 将整数元素的序列，转为字符串型
# [1,2,3,4]—>["1","2","3","4"]
l = map(str, [1, 2, 3, 4])
print(list(l))
'''
reduce() 函数会对参数序列中元素进行累积。
注意：Python3.x reduce() 已经被移到 functools 模块里，如果我们要使用，需要引入 functools 模块来调用 reduce() 函数：
reduce() 函数语法：
    reduce(function, iterable[, initializer])

参数
    function -- 函数，有两个参数
    iterable -- 可迭代对象
    initializer -- 可选，初始参数
返回值
    返回函数计算结果。

功能
    一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列的写一个元素累积运算

实例
    reduce(f,[a,b,c,c])
    f(f(f(a,b),c),d)
'''

# 求一个序列的和
list2 = [1, 2, 3, 4, 5]


def mySum(x, y):
    return x + y


r = reduce(mySum, list2)
print(r)
