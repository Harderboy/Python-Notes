'''
回文数
    定义:
        回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。(对称的数)

符合条件:
    一位数 0-9
    必须是整数,排除小数
    不能为负数:-121  121-
    整数第一位不能为0,终端输入合法,直接传参不合法,报错如下:    
    res4 = a.isPalindrome(010)
                            ^
    SyntaxError: leading zeros in decimal integer literals are not permitted;
    use an 0o prefix for octal integers
'''
while True:
    s = input("请重新输入一个整数：")
    if s[0] != '-' and s[0] > '0' and s.isdigit():
        break
    else:
        print("输入有误！")

for i in range(int(len(s) / 2)):
    if s[i] != s[len(s) - 1 - i]:
        print("%s 不是回文数！" % s)
        break
else:
    print("%s 是回文数！" % s)


# 封装成类
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


a = Solution()
res1 = a.isPalindrome(123)
print(res1)
res2 = a.isPalindrome(121)
print(res2)
res3 = a.isPalindrome(-121)
print(res3)
res4 = a.isPalindrome(10)
print(res4)
res5 = a.isPalindrome(0)
print(res5)
