import re

# '/' 斜杠
# '\' 转义字符
r'''
re.match函数
    扫描整个字符串，返回从起始位置成功的匹配
语法：
    re.match(pattern, string, flags=0)
参数：
    pattern 匹配模式。
    string 待匹配的字符串。
    flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
功能：
    re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

flags 标志位:
    re.I	使匹配对大小写不敏感
    re.L	做本地化识别（locale-aware）匹配
    re.M	多行匹配，影响 ^ 和 $
    re.S	使 . 匹配包括换行在内的所有字符
    re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''

# www.baidu.com
# span()：返回一个元组包含匹配 (开始,结束) 的位置
print(re.match('www', "www.baidu.com").span())
print(re.match('www', "ww.baidu.com"))
print(re.match('www', "baike.www.com"))
print(re.match('www', "wwW.baidu.com"))
print(re.match('www', "wwW.baidu.com", re.I))
print(re.match('www', "wwW.baidu.com", flags=re.I))

print("-" * 22)

r'''
re.search方法
语法：
    re.search(pattern, string, flags=0)
功能：
    扫描整个字符串并返回第一个成功的匹配。
    匹配成功re.search()方法返回一个匹配的对象，否则返回None。
'''

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
print(re.search('cn', 'www.runoob.com'))
# a = re.search('cn', 'www.runoob.com')
# print(a)
# print(not a)
# b = re.search('com', 'www.runoob.com')
# print(b)
# print(not b)

print("-" * 22)

r'''
findall
功能：
    在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。
语法格式为：
    re.findall(pattern, string, flags=0)
    或
    pattern.findall(string[, pos[, endpos]])
参数：
    pattern 匹配模式。
    string 待匹配的字符串。
    pos 可选参数，指定字符串的起始位置，默认为 0。
    endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''

print(re.findall("sunck", "good man is sunck!Sunck is nice", flags=re.I))


print('--------匹配单个字符与数字---------')
r'''
.   匹配除换行符以外的任意字符
[]  字符集合，表示匹配方括号中所包含的任意一个字符
[1-9]  匹配1-9中的任意一个数字
[a-zA-Z0-9_]  匹配任何字母、数字和下划线
[^...]  ^ 脱字符 表示不匹配集合中的字符 （不在[]中的字符）
[^0-9] 
\d	匹配任意数字，等价于 [0-9]
\D	匹配任意非数字 等价于 [^\d]
\w	匹配数字字母下划线 等价于 [a-zA-Z0-9_]
\W	匹配非数字字母下划线 等价于 [^a-zA-Z0-9_]
\s	匹配任意空白字符，等价于 [ \t\n\r\f]（空格、制表、换行、回车、换页）
\S	匹配任意非空字符 等价于 [^ \t\n\r\f]

'''

print(re.findall(r"[^\d]", "_sunck is good 123"))


print('--------锚字符（边界字符）---------')
r'''
^   行首匹配，和在[]中的^ 含义不同  ^sunck：以sunck开头
$   行尾匹配 man$：以man结尾的字符串
\A  匹配字符串开始，它与^的区别：它只匹配整个字符串的行首，即使在re.M模式下也不会匹配其他行的行首
\Z  匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。 它与$的区别：它只匹配整个字符串的行尾，即使在re.M模式下也不会匹配其他行的行尾
\b  匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'
\B  匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'

'''

print(re.search("^sunck", "sunck is good man"))
print(re.search("man$", "sunck is good man"))

print('-' * 22)
print(re.findall("^sunck", "sunck is good man\nsunck is good man"))
print(re.findall("^sunck", "sunck is good man\nsunck is good man", re.M))
print(re.findall(r"\Asunck", "sunck is good man\nsunck is good man"))
print(re.findall(r"\Asunck", "sunck is good man\nsunck is good man", re.M))

print('-' * 22)
print(re.findall("man$", "sunck is good man\nsunck is good man"))
print(re.findall("man$", "sunck is good man\nsunck is good man", re.M))
print(re.findall(r"man\Z", "sunck is good man\nsunck is good man"))
print(re.findall(r"man\Z", "sunck is good man\nsunck is good man", re.M))

print('-' * 22)
print(re.search(r"er\b", "never die"))
print(re.search(r"er\b", "verb"))
print(re.search(r"er\B", "never die"))
print(re.search(r"er\B", "verb"))


print('--------匹配多个字符---------')
'''
(xyz)  匹配小括号中的xyz（作为一个整体去匹配）
x？     匹配0个或者1个x
x*      匹配0个或者任意多个x
x+      匹配至少一个x
x{n}    匹配确定的n个x（n为一个非负整数）
x{n，}  匹配至少n个x
x{n,m}  匹配至少n个最多m个x，注意n <= m
x|y     匹配x或者y

'''

# 非贪婪匹配（尽可能少的匹配）
print(re.findall(r'a?', "aaaa"))
# 贪婪匹配（匹配尽可能多的匹配）
print(re.findall(r'a*', "aaabaaa"))
# 贪婪匹配
print(re.findall(r'a+', "aaabaaaaa"))
print(re.findall(r'a{3}', "aaaabaa"))
# 贪婪匹配
print(re.findall(r'a{3,}', "aaaaaaabaa"))
print(re.findall(r'a{3,6}', "aaaaabaaa"))
print(re.findall(r'((s|S)unck)', "sunck--Sunck"))

print('-' * 22)
# 需求，提取sunck......man
str = "sunck is a good man!sunck is a nice man!sunck is a very handsome man"
res = re.findall(r"^sunck.*man$", str)  # .* 贪婪匹配
print(res)
res2 = re.findall(r"^sunck.*?man$", str)
print(res2)
res3 = re.findall(r"sunck.*?man", str)
print(res3)


print('--------特殊---------')
'''
*? +? x?  最小匹配，解贪婪匹配 从"贪婪"表达式转换为"非贪婪"表达式或者最小匹配。
(?:x)   类似（xyz），但不表示一个组

'''
# 例子
# 注释 /*  part1 */ /*  part2 */
# '\n' 转义成换行符 "\\n" 不转义 '\\' 两个转义字符表示不转义
print(re.findall(r"/\*.*\*/", "/*  part1 */ /*  part2 */"))
print(re.findall(r"/\*.*?\*/", "/*  part1 */ /*  part2 */"))