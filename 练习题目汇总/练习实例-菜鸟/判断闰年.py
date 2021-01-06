# coding=utf-8
'''
四年一闰，百年不闰，四百年再闰。

核心代码：
    if((n%4 == 0 && n%100 != 0) || n %400 == 0)

python中逻辑运算符：and or not
        比较运算符：== !=

'''

try:
    year = int(input("请输入一个年份："))
    if (year > 0):
        if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            print("%d 年是闰年" % year)
        else:
            print("%d 年不是闰年" % year)
    else:
        print("输入有误！")

except:
    print("输入有误！")
