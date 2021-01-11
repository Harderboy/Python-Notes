'''
素数：
    素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。
    1不是素数，最小的质数是2
'''

min = int(input("请输入区间最小值："))
max = int(input("请输入区间最大值："))

if min <= 2:
    print("[%d,%d]之内的素数有：" % (min, max))
    print(2)
    for num in range(3, max + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
else:
    print("[%d,%d]之内的素数有：" % (min, max))
    for num in range(min, max + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
