#!/usr/bin/python3

dict = {'Name': 'Runoob', 'Age': 27}

print("Age 值为 : %s" % dict.get('Age'))
print("Sex 值为 : %s" % dict.get('Sex', "NA"))
print(dict.get('Sex'))
print(dict['Age'])

a = 0 or 1
print(a)

print('-----')


def A():
    print(1)
    print(2)


m = A()
print(m)

print("-" * 22)
n = 1
print('n:%s' % n)
m = 'dadf'
# print('n:%d' % m) 报错
print('n:%s' % m)

print('-----')


def myfun():
    return 1, 2, 3


a = myfun()
print(a)
print(type(a))
a, b, c = myfun()
print("a:", a)
print(type(a))
print('b:', b)
print("c:", c)

d = 1, 2  # 等同于 d = (1,2)
print(d)
print(type(d))