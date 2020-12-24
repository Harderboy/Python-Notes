##  Python爬虫学习笔记

- 使用的python版本为：Python 3.5.2

### 一、 python基础部分学习
   
   - python语法

### 二、Python爬虫学习

#### 1. 什么是爬虫

- 模拟浏览器打开网页，获取需要的数据

#### 2. 爬虫的基本方法

- 发起请求：向目标``url`` 发送``Request``，等待服务器响应
- 获取响应内容：服务器响应收到``Response``，就是所要获得的页面内容，类型可能是HTML,Json字符串，二进制数据（图片或者视频）等类型
- 解析内容：对返回的页面内容进行解析
- 保存数据：可以将获取的数据保存为文本，数据库以及其他特定格式的文件

#### 3. 解析数据的方法

- 正则表达式解析处理
- Xpath解析处理
- BeaitifulSoup解析处理

还有其他几种方法，尚未学习

#### 4. 爬虫框架

- 参考链接：[8个python爬虫框架](https://segmentfault.com/a/1190000015131017)

### 三、urllib

官方文档：[urlli](https://docs.python.org/3/library/urllib.htmlhttps://docs.python.org/3/library/urllib.html)

#### 1. urllib使用

- urllib有以下几个模块：
    - urllib.request
    - urllib.error
    - urllib.parse
    - utllib.robotparser

- urllib使用

```python
import urllib.request
import urllib.parse
import urllib.error
import socket
from urllib.parse import urlencode

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding = 'utf8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post',data = data)
print(response)
print(response.read().decode('utf-8'))
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout = 0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('超时')

data1 = {
    "name":"zhaohu",
    "adress":"beijing"
    }

url = 'http://httpbin.org/get'+urlencode(data1)
print(url)
```
![](./images/3_1.png)

- 从这段代码中，可以看到``urllib``各个模块以及参数的使用

    - ``urllib.request``：请求模块。它的``urlopen``函数返回值是``http.client.HTTPResponse``对象，其中的``read()``函数可以获得页面内容，一般而言，``read()``函数后还需要``decode()``函数，因为返回的网页内容实际上是没有被解码的，所以需要指定解码方式对页面进行解码。
    - ``urllib.parse``：URL解析模块。获取URL的参数，然后进行需要的处理。比如本段代码中的拼接。
    - ``urllib.error``:urllib.request引发的异常类。
    - ``timeout``：参数的作用是在网络情况不好或者服务器异常的情况下，或者请求异常设置的一个超时时间。

### 四、Requests库

- 官方文档：[Requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

#### requests库的使用

```python
import requests
response = requests.get("http://www.baidu.com")
print(response.status_code)
print(response.headers)
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))
```
- 在以上这段代码中
    - ``get``方式获页面内容
    - ``response.status_code``返回状态码
    - ``response.headers``返回是响应头部信息
    - ``response.text``返回的是页面内容
    - ``response.cookies``获取响应中的cookie信息
    - ``response.content``返回二进制格式的页面信息，因为有些页面用response.text返回会出现乱码，所以通过二进制获取页面内容再进行编码就可以解决乱码问题。

- 还有其他的请求方式,如``post``,``put``等
- 有些网站无法直接进行访问，需要定制``headers``信息,请求头部信息可以直接通过浏览器抓包进行查看。
```python
import requests
headers = {"user-agent"}:{Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36}
response = requests.get(url，headers=headers)
print(response.text)
```

### 五、python正则表达式

#### 正则表达式详解

- 参考链接：[廖雪峰教程-正则表达式](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000)

#### re模块

- re.match():尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
```
re.match(pattern, string, flags=0)
pattern 匹配的正则表达式
string 要匹配的字符串
flags 标志位，用来控制正则表达式匹配
```

- re.search():扫描整个字符串并返回第一个成功的匹配。
```
re.search(pattern, string, flags=0)
```

- re.sub():用于替换字符串中的匹配项
```
re.sub(pattern, repl, string, count=0, flags=0)
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
```

- re.compile():用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
```
re.compile(pattern[, flags])
pattern : 一个字符串形式的正则表达式

flags : 可选，表示匹配模式，比如忽略大小写
```

- findall:在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
```
findall(string[, pos[, endpos]]) //string : 待匹配的字符串。pos : 可选参数，指定字符串的起始位置，默认为 0。endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
```

#### 实例：爬取豆瓣读书

```python
import requests
import re
header = {
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
content = requests.get('https://book.douban.com/',headers = header).text
#print(content)

#pattern = re.compile('<li.*?cover.*?href="(.*?)".*?alt="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?alt="(.*?)".*?info.*?author">(.*?)</div>.*?</li>',re.S)
#pattern = re.compile('<li.*?cover.*?href="(.*?)".*?alt="(.*?)".*?info.*?<span."author">(.*?)</div>.*?"title">(.*?)</h4>.*?</li>',re.S)
results = re.findall(pattern, content)
#print(results)

for result in results:
    url,name,author = result
    author = re.sub('\s','',author)
    print(url,name,author)
```

- 以上代码是用正则表达式实现爬取[豆瓣读书](https://book.douban.com/)的页面信息
![](./images/3_2.png)

### 六、Xpath

``Xpath``,全称``XML Path Language``，即XML路径语言，它是一门在XML文档中查找信息的语言。它最初是用来搜寻XML文档的，但是它同样适用于HTML文档的搜索。

- 具体用法可参考知乎文章：
[学爬虫利器XPath,看这一篇就够了](https://zhuanlan.zhihu.com/p/29436838)

#### Xpath实例

```python
import requests
from lxml import etree

url = "https://nvd.nist.gov/vuln/detail/CVE-2018-18258"
header = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def getOnePage(url):
    r = requests.get(url)
    return r.text

def parseOnePage(text):
    html = etree.HTML(text)
    cpes = html.xpath('//div[@class ="configurations"]/span/a/text()')
#    hype = html.xpath('//table[@class = "table table-striped table-condensed table-bordered detail-table"]')
    print(cpes)

text = getOnePage(url)
parseOnePage(text)
```

- 以上代码是获取[
CVE-2018-18258 Detail](https://nvd.nist.gov/vuln/detail/CVE-2018-18258)里的cpe字段信息。结果如下：
![](./images/3_3.png)

### 七、BeautifulSoup库

- BeautifulSoup库是爬虫非常强大的一个库

#### BeautifulSoup库的使用

- BeautifulSoup库的具体用法可参考：[Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#beautiful-soup-4-2-0)

#### 使用实例

```python
import requests
from bs4 import BeautifulSoup

def get_html(url,data):
    response = requests.get(url,data)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    cves = soup.find("tbody")
    trs = cves.find_all("tr")
    for tr in trs:
        counts = tr.th.strong.a.text
#        with open('./cve.txt','a') as f:
#            f.write(counts+'\n')
        scores = tr.select("td")[1]
        length = len(scores)
        if length > 3:
            countt = scores.select("span")[0].text.strip()
            countr = scores.select("span")[1].text.strip()
            with open('./cve.txt','a') as f:
                f.write(counts+'\t'+countt+'\t'+countr+'\n')
        else:
            countt = scores.select("span")[0].text.strip()
            with open('./cve.txt','a') as f:
                f.write(counts+'\t'+countt+'\n')

def main():
    num = 0
    base_url = "https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=drupal&search_type=all"
    for i in range(1,53):
        data = {
            "startIndex":num
        }
        num = num + 20
        html = get_html(base_url,data)
        parse_html(html)

if __name__=='__main__':
    main()
```

- 这段代码的是爬取[NVD-Drupal](https://nvd.nist.gov/vuln/search/results?form_type=Basic&results_type=overview&query=drupal&search_type=all&startIndex=1020)里的所有``CVE-ID``和``CVSS评分``信息。具体结果如[cve-info](./images/cve.txt)所示。