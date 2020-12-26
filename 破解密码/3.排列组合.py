import itertools

# 切勿直接运行
mylist = list(
    itertools.product(
        "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM",
        repeat=3))

# print(mylist)
print(len(mylist))
