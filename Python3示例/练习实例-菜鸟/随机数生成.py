import random

print("-" * 22)

# random.randint(a,b) 函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。
a = random.randint(0, 9)
print("输出0~9随机整数:", a)

print("-" * 22)

# random() 方法返回随机生成的一个实数，它在[0,1)范围内。
b = random.random()
print("输出0~1随机实数:", b)

print("-" * 22)

# random.randrange ([start,] stop [,step]) 从给定的范围返回随机项。
c = random.randrange(1, 100, 2)
print("输出1~100间隔为2的随机数:", c)

print("-" * 22)

# random.choice(seq) 方法返回一个列表，元组或字符串的随机项。seq：可以是一个列表，元组或字符串。
myList = [1, 2, 3, 5, 9]
d = random.choice(myList)
print("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素:", d)
print("从 range(100) 返回一个随机数:", random.choice(range(100)))
print("从字符串中 'Runoob' 返回一个随机字符:", random.choice('Runoob'))

print("-" * 22)

# range(stop)
# range(start, stop[, step])
# range() 函数返回的是一个可迭代对象（类型是对象）
# for i in range(5):
#     print(i)
