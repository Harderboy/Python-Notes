# 排序：冒泡、选择 快速 插入 计数器
'''
sorted() 函数对所有可迭代的对象进行排序操作。
语法
    sorted(iterable, key=None, reverse=False)

参数说明：
    iterable -- 可迭代对象。
    key -- 主要是用来接收函数来实现自定义排序规则，具体的函数的参数就是取自于可迭代对象中，
    reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）

返回值
    返回重新排序的列表。
'''
'''
list.sort()对比sorted()
    1.使用 list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）。通常这个方法不如sorted()方便
      如果你不需要原始的 list，list.sort()方法效率会稍微高一些。
    2.另一个区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable。
'''

# 普通排序
list1 = [4, 7, 8, 6, 3]
list1.sort()
# list2 = list1.sort()
print(list1)
# print(list2)
list3 = sorted(list1)
print(list3)

print("-" * 22)

# 按绝对值大小排序，元素值不发生变化
list4 = [4, -9, -6, 5, 3]

# key接收函数来实现自定义排序规则
list5 = sorted(list4, key=abs)  # [3, 4, 5, -6, -9]
# map处理过的序列元素经过函数处理发生了变化，不同于key接收函数的方式
list6 = sorted(map(abs, list4))  # [3, 4, 5, 6, 9]
print(list4)
print(list5)
print(list6)

print("-" * 22)

# 降序
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
example_list2 = sorted(example_list, reverse=True)
print(example_list)
print(example_list2)

print("-" * 22)

# 按ascii值大小排序
list7 = ['d', 'c', 'd', 'a']
list8 = sorted(list7)
print(list8)

list9 = ['b333', 'a1111', 'c22', 'd54561']
list10 = sorted(list9)
print(list10)

print("-" * 22)

# 按字符串长度排序
list9 = ['b333', 'a1111', 'c22', 'd54561']
list11 = sorted(list9, key=len)
print(list11)


# 自定义函数返回字符串长度
def myLen(str):
    return len(str)


list12 = sorted(list9, key=myLen)
print(list12)

print("-" * 22)

# sorted() 函数可以接收任何的 iterable。对字典的key进行排序，因为key值是唯一的
list13 = sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
print(list13)