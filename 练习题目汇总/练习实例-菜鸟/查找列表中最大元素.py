# coding=utf-8
'''
定义一个数字列表，并查找列表中的最大元素。

查找列表中最小元素，思路类似
sorted()方法默认升序
'''

list1 = [10, 20, 4]
list2 = [10, 20, 4]

# 方法1：list.sort()方法，但是这个方法会修改原始的 list
list1.sort()
print(list1)
print("最大元素为:", list1[-1])

# 方法2：内置函数sorted()
res = sorted(list2)
print("最大元素为:", res[-1])

# 方法3：使用内置函数max()
# max() 方法返回给定参数的最大值，参数可以为序列。
# max(x, y, z, ....)
# max(0, 100, -400))
res1 = max(list2)
print("最大元素为:", res1)
