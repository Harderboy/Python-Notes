'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
    输入：nums = [3,2,4], target = 6
    输出：[1,2]
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while True:
            if i < len(nums):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
            i += 1


'''
参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤。
'''


def twoSum(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]


# 其他思路
'''
index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
list.index(x[, start[, end]])

参数
    x-- 查找的对象。
    start-- 可选，查找的起始位置。
    end-- 可选，查找的结束位置

返回值
该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。
'''