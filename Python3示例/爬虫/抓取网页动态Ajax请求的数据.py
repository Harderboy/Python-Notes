import urllib.request
import ssl
import json
import time


def ajaxCrawler(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    '''
    # 使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    '''

    response = urllib.request.urlopen(req)
    # print(type(response))
    # print(type(response.read()))
    jsonStr = response.read().decode("utf-8")
    # print(type(jsonStr))
    jsonData = json.loads(jsonStr)
    print(type(jsonData))
    return jsonData


if __name__ == "__main__":
    for i in range(1, 6):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
            i * 20) + "&limit=20"
        time.sleep(1)
        info = ajaxCrawler(url)
        print(info)
        print(len(info))
