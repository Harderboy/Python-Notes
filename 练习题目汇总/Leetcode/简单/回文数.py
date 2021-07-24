'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:

你能不将整数转为字符串来解决这个问题吗？
'''


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    def isPalindrome(self, x):
        s = str(x)
        if len(s) == 1 and '0' <= s <= '9':
            return True
        elif s[0] == '-' or s[0] == '0':
            return False
        elif s.isdigit():
            for i in range(int(len(s) / 2)):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            else:
                return True
        else:
            return False


# 大神写法
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False