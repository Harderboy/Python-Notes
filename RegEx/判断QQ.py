import re

# pat = r'^[1-9]\d{5,9}'
# re_QQ = re.compile(pat)
# str1 = "1324631884"
# res = re_QQ.match(str1)
# print(res)
re_QQ = re.compile(r'^[1-9]\d{5,9}')
print(re_QQ.match("1324631884"))
print(re_QQ.match("13246318842251525763"))
print(re_QQ.search("13246318842251525763"))
re_QQ_2 = re.compile(r'^[1-9]\d{5,9}$')  # 以5到9个数字结尾
print(re_QQ_2.match("1324631884"))
print(re_QQ_2.match("13246318842251525763"))
print(re_QQ_2.search("13246318842251525763"))