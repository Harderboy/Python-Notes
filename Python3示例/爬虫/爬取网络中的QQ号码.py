import urllib.request
import os
import re
from collections import deque
import time


def bytesFileWriter(htmlBytes, desPath):
    with open(desPath, "wb") as f:
        f.write(htmlBytes)


def strFileWriter(htmlBytes, desPath):
    with open(desPath, "w") as f:
        f.write(str(htmlBytes))


def getHtmlBytes(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read()


def qqCrawler(url, desPath):
    htmlBytes = getHtmlBytes(url)

    # bytesFileWriter(htmlBytes,r'C:\Users\liu heng\Desktop\Python学习笔记\文件处理\爬取QQ号码\file1.html')
    # strFileWriter(htmlBytes,r'C:\Users\liu heng\Desktop\Python学习笔记\文件处理\爬取QQ号码\file2.html')

    htmlStr = str(htmlBytes)

    pat_qq = r'[1-9]\d{8,10}'
    re_qq = re.compile(pat_qq)
    qqsList = re_qq.findall(htmlStr)
    # print(qqsList)
    # print(len(qqsList))
    # 去重 set()
    qqsList = list(set(qqsList))
    # print(qqsList)
    # print(len(qqsList))
    for qqStr in qqsList:
        with open(desPath, "a") as f:
            f.write(qqStr + "\n")

    # 查找网址
    # 查找网址的正则表达式：
    # (((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1-4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)
    pat_url = r'(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1-4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)'
    re_url = re.compile(pat_url)
    urlsList = re_url.findall(htmlStr)
    # 去重 set()
    urlsList = list(set(urlsList))
    # print(urlsList)
    # print(len(urlsList))
    # rint(urlsList[102])
    desPath2 = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\爬取QQ号码\url.txt"
    # urlsList中元素为列表，且第一位为url
    for urlStr in urlsList:
        with open(desPath2, "a") as f:
            f.write(urlStr[0] + "\n")
    return urlsList


def centerControl(url, desPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        time.sleep(2)
        urlList = qqCrawler(targetUrl, desPath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)


if __name__ == "__main__":
    url = "https://www.douban.com/group/topic/20285003/?start=100"
    desPath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\爬取QQ号码\qq.txt"
    # qqCrawler(url, desPath)
    centerControl(url, desPath)
