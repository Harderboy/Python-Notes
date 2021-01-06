# coding=utf-8
'''
定义一个数字列表，并计算列表元素之和。
'''

list1 = [11, 5, 17, 18, 23]

# 方法1：遍历
# for循环或者while循环
total = 0
for ele in range(0, len(list1)):
    total = total + list1[ele]

print("循环求得的列表元素之和为:", total)


# 方法2：使用递归
def sumOfList(list, size):
    if size == 0:
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)


sum_list = sumOfList(list1, len(list1))
print("递归求得的列表元素之和为:", sum_list)


# 方法3：reduce()函数
# 需要引入 functools 模块来调用 reduce()函数
from functools import reduce


res = reduce(lambda x, y: x + y, list1)
print("reduce函数求得的列表元素之和为:", res)

# 方法4：sum()内置函数
# sum() 方法对序列进行求和计算。
'''
sum(iterable[, start])
参数
iterable -- 可迭代对象，如：列表、元组、集合。
start -- 指定相加的参数，如果没有设置这个值，默认为0。

>>>sum([0,1,2]) 
3
>>> sum((2, 3, 4), 1)        # 元组计算总和后再加 1
10
>>> sum([0,1,2,3,4], 2)      # 列表计算总和后再加 2
12
'''
'''
报错信息：
    print("sum函数求得的列表元素之和为：", sum(list1))
TypeError: 'int' object is not callable

原因：
    前边使用了变量sum，要避免这种情况，不要将 Python 关键字和函数名用作变量名

'''
print("sum函数求得的列表元素之和为:", sum(list1))