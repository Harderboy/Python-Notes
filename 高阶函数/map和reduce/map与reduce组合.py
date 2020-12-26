from functools import reduce

# map()和reduce()搭配使用
# 将字符串转成对应字面量数字


def strToInt(str):
    def fc(x, y):
        return x * 10 + y

    def fs(chr):
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

    return reduce(fc, map(fs, list(str)))


str = "12367"
a = strToInt(str)
print(a)
print(type(a))


# 制作自己的map
def myMap(func, list):
    resList = []
    for parase in list:
        res = func(parase)
        resList.append(res)
    return resList


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

res = myMap(charToInt, list1)
print(res)
print(type(res))
