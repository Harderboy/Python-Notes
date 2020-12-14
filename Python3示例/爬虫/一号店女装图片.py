import urllib.request
import re
import os


def imageCrawler(url, desPath):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    # 写入文件时，使用 HtmlStr = response.read() 不会产生乱码
    HtmlStr = response.read().decode("utf-8")

    # with open(r'C:\Users\liu heng\Desktop\Python学习笔记\文件处理\file\yhd.html',
    #          "wb") as f:
    #    f.write(HtmlStr)

    # pat = r'<img src="//(.*?)" width="102" height="36">'
    pat = r'<img width="220" height="220" data-img="1" data-lazy-img="//(.*?)" />'
    re_image = re.compile(pat)
    imageList = re_image.findall(HtmlStr)
    # print(imageList)
    # print(len(imageList))
    # print(imageList[0])

    num = 1
    for imageUrl in imageList:
        path = os.path.join(desPath, str(num) + ".jpg")
        num += 1
        # 把图片下载到本地
        url = "http://" + imageUrl
        urllib.request.urlretrieve(url, filename=path)


if __name__ == "__main__":
    url = "https://search.jd.com/Search?keyword=%E8%BF%9E%E8%A1%A3%E8%A3%99%E7%A7%8B%E5%86%AC&enc=utf-8&suggest=2.def.0.base&wq=lianyi&pvid=5d3f569f308a43388a7807e7bca04af1"
    desPath = r"C:\Users\liu heng\Desktop\Python学习笔记\文件处理\yhd_images"
    imageCrawler(url, desPath)
