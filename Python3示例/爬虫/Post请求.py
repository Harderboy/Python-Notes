'''
特点：把参数进行打包，单独传输

优点：数量大，安全（当对服务器数据进行修改时建议使用post）
缺点：速度慢

'''

import urllib.request
# 对参数进行打包
import urllib.parse

url = ""

data = {}

# 对发送的数据进行打包
postData = urllib.parse.urlencode(data).encode("utf-8")

# 请求体
req = urllib.request.Request(url, data=postData)

# 请求
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
