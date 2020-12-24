import urllib.request

urllib.request.urlretrieve(
    "http://www.baidu.com",
    filename=r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\file\file2.html")

# urlretrieve 在执行的过程当中，会产生一些缓存
# 清除缓存
urllib.request.urlcleanup()
