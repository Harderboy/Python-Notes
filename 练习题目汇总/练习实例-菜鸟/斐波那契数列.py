'''
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
'''

# 方法1：循环
num_count = int(input("斐波那契数列需要几项："))
n1 = 0
n2 = 1
count = 2

if num_count <= 0:
    print("请输入一个正数！")
elif num_count == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ',', n2, sep='', end='')
    while count < num_count:
        tmp = n1 + n2
        print(',', sep='', end='')
        print(tmp, end='')
        # n1 = n2
        # n2 = tmp
        n1, n2 = n2, tmp
        count += 1


# 方法2：递归
def fab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


nums = int(input("斐波那契数列需要几项："))
if nums <= 0:
    print("请输入一个整数!")
else:
    print("斐波那契数列：")


# i = 1
# while i <= nums:
#     print(fab(i), end=',')
#     i += 1


for i in range(1, nums+1):
    print(fab(i), end=',')