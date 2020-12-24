import urllib.request
import re
import time


def jokeCrawler(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)

    HTML = response.read().decode("utf-8")

    # path = r'C:\Users\liu heng\Desktop\Python学习笔记\文件处理\file\file3.html'
    # with open(path, "w", encoding="utf-8") as f:
    #    f.write(HTML)

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)
    divList = re_joke.findall(HTML)
    # print(divList)
    # print(len(divList))
    dict = {}
    for div in divList:
        # 用户名
        re_u = re.compile(r'<h2>(.*?)</h2>', re.S)
        usernames = re_u.findall(div)
        # print(username)
        # print(type(username))
        username = usernames[0]
        # print(username)
        # 段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        jokes = re_d.findall(div)
        joke = jokes[0]
        print(joke)

        dict[username] = joke

    return dict


if __name__ == "__main__":
    for i in range(1, 4):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        info = jokeCrawler(url)
        print(len(info))
        time.sleep(0.5)
        for k, v in info.items():
            print(k, v)
