import itertools

mylist = list(itertools.permutations([1, 2, 3, 4], 3))
# 4*3*2
print(mylist)
print(len(mylist))
