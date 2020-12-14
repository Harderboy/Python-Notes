import urllib.request
import random

url = "http://www.baidu.com"
"""
# 模拟请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

# 设置请求体
req = urllib.request.Request(url, headers=headers)

# 发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
"""

agentList = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/27.0.1453.10 Mobile/10B350 Safari/8536.25"
]

# random.choice(seq) 方法返回一个列表，元组或字符串的随机项。seq:可以是一个列表，元组或字符串。
agentStr = random.choice(agentList)

# 向请求体里添加了一个User-Agent
# urllib.request.Request(url[,headers=])，其中headers参数为字典类型
# 通过add_header()方式添加键值对:req.add_header("User-Agent", agentStr)
req = urllib.request.Request(url)
req.add_header("User-Agent", agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))