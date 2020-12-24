# -*- coding: UTF-8 -*-

# 质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。
# 自然数：零和正整数（大于零的整数）。
# num = int(float(input("请输入一个数字：")))

num = int(input("请输入一个数字："))

if num > 1:
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            print("输入的数 %d 不是质数" % num)
            print("%d * %d = %d" % (i, num / i, num))
            break
    else:
        print("输入的数 %d 是质数" % num)
else:
    print("输入的数 %d 不是质数" % num)

# 另外的思路：i += 1

# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。可以和 else 搭配使用，如上示例

# for循环的一般格式如下：

# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

# 输入数字为浮点数是报错
# ValueError: invalid literal for int() with base 10: '0.6'

# 解决方法：
# input函数返回的是string类型，即字符串
# int函数将字符串形式的数值转换为整数时，字符串中只能包含数字（不能为浮点数）
# 所以正确的方法应该是先将字符串转换成float（不管你输的是整数还是浮点都可以通过），再将float转换成int
# float() 函数用于将整数和字符串转换成浮点数。
# a=int(float(input()))
# 但是这种方法也存在问题：
# int 对 float 类型的数字向下取整
# >>> int(2.5)
# 2

# >>> int("3.14",8)
# >>> int("1.2")
# 均报错，str须为整数
