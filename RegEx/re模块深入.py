import re

print('--------字符串切割---------')
'''
字符串切割
'''

str1 = "sunck         is good man"
print(str1.split(' '))
print(re.split(r" +", str1))

print('--------finditer函数---------')
'''
re.finditer()
功能：
    和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
语法：
    re.finditer(pattern, string, flags=0)

'''

str2 = "sunck is a good man!sunck is a nice man!sunck is a very handsome man"
d = re.finditer(r'(sunck)', str2)
# print(d)
while True:
    try:
        l = next(d)
        print(l)
    except StopIteration as e:
        break

print('--------字符串替换与修改---------')

'''
检索和替换
    Python 的re模块提供了re.sub和re.subn用于替换字符串中的匹配项。
语法：
    re.sub(pattern, repl, string, count=0, flags=0)
    re.subn(pattern, repl, string, count=0, flags=0)
参数：
    pattern: 正则中的模式字符串。
    repl: 指定的用来替换的字符串，也可为一个函数。
    string: 要被查找替换的原始字符串，目标字符串。
    count: 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
    flags: 编译时用的匹配模式，数字形式。
功能：
    在目标字符串中以正则表达式的的规则匹配字符串，再把他们替换成指定字符串，可以指定替换次数。
区别：
    前者返回一个被替换的字符串，后者返回一个元组，元组中第一个元素为被替换的字符串，第二个元素表示被替换的次数。
'''

str3 = "sunck is a good good good man"
res = re.sub(r"(good)", "nice", str3)
print(res)
print(type(res))
res2 = re.sub(r"(good)", "nice", str3, count=2)
print(res2)

res3 = re.subn(r"(good)", "nice", str3)
print(res3)
print(type(res3))

print('--------分组---------')

'''
分组：
    除了简单的判断是否匹配之外，正则表达式还有提取字串的功能，用()表示的就是提取的分组

'''

str4 = "010-53247654"
m = re.match(r'\d{3}-\d{8}', str4)
print(m)

m1 = re.match(r'(\d{3})-(\d{8})', str4)
print(m1)
# 使用序号获取对应组的信息，group(0)一直代表原始的字符串，及str4
print(m1.group(0))
print(m1.group(1))
print(m1.group(2))
# print(m1.group(3))
# 查看匹配的各组的情况，返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
print(m1.groups())

print('-----------------')

m2 = re.match(r'((\d{3})-(\d{8}))', str4)
print(m2)

print(m2.group(0))
print(m2.group(1))
print(m2.group(2))
print(m2.group(3))

# 给组起名字
m3 = re.match(r'(?P<first>\d{3})-(?P<last>\d{8})', str4)
print(m3)
# 使用序号获取对应组的信息，group(0)一直代表原始的字符串，及str4
print(m3.group(0))
print(m3.group(1))
print(m3.group("first"))
print(m3.group(2))
# print(m1.group(3))


print('--------编译正则表达式---------')

r'''
compile 函数
    compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
    1.编译正则表达式，如果正则表达式本身不合法，会报错
    2.用编译后的正则表达式去匹配对象
语法格式为：
    re.compile(pattern[, flags])
参数：
    pattern : 一个字符串形式的正则表达式
    flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
        re.I 忽略大小写
        re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
        re.M 多行模式
        re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
        re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
        re.X 为了增加可读性，忽略空格和' # '后面的注释

re模块调用的方法，编译后的正则表达式对象（re对象）也可调用，区别在于方法（函数）中无需 pattern 参数，举例如下：
    pat = r'^1(([3578]\d)|(47))\d{8}$'
    re_telephon = re.compile(pat)
    # 其他参数不一一列举
    re_telephon.match(string)
    re_telephon.findall(string)
    re_telephon.finditer(string)
    re_telephon.split(string)
    re_telephon.sub(string)

'''

pat = r'^1(([3578]\d)|(47))\d{8}$'
str5 = "13022364644"
print(re.match(pat, str5))
# 编译成正则表达式对象
re_telephon = re.compile(pat)
print(re_telephon.match(str5))
# re_telephon.split(str5)