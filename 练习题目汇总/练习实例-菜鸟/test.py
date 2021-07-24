# import itertools
# for x in itertools.permutations([1, 2, 3, 4], 3):
#     print(x)

# nums = int(input("斐波那契数列需要几项："))
# if nums <= 0:
#     print("请输入一个整数!")
# else:
#     print("斐波那契数列:")

# def fab(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fab(n - 1) + fab(n - 2)

# # i = 1
# # while i <= nums:
# #     print(fab(i), end=',')
# #     i += 1

# for i in range(1, nums+1):
#     print(fab(i), end=',')

# seqString = 'Runoob'
# print(reversed(seqString))
# print(type(reversed(seqString)))
# print(str(reversed(seqString)))
# seq = ("r", "u", "n", "o", "o", "b")
# print(type(seq))
# print(str(seq))
# dict = {'runoob': 'runoob.com', 'google': 'google.com'}
# print(str(dict))
# L=['Google', 'Runoob', 'Taobao']
# print(L[0])
# print(L[::-1])

# print([chr(x) for x in range(ord('A'), ord('A') + 6)])
# for x in range(ord('A'), ord('A') + 6):
#     print(x)

# def quickSort(arr):
#     if len(arr) < 2:  # 不用进行排序
#         return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr if i < pivot]
#         middle = [x for x in arr if x == pivot]
#         great = [i for i in arr if i > pivot]
#         return quickSort(less) + middle + quickSort(great)

# arr = [4, 1, 5, 2, 41, 4, 24, 5]
# print("原始数据：", arr)
# print("排序后的数据：", quickSort(arr))

# print([[0 for i in range(5+1)]for j in range(5+1)])

print('bc' in 'abc')
print('' == None)
print(type(None))