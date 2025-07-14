# import json
from bs4 import BeautifulSoup
import requests
import re

# dynamic.xingsudaili.com:10010
# pv.souhu.com/cityjson


def getIp():
    response = requests.get(url='http://www.baidu.com')
    print(response.text, response.status_code)


def loadImage(url):
    response = requests.get(url)
    with open('image.png', 'wb') as f:
        f.write(response.content)


def souhu():
    # proxy = {
    #     'http': 'http://dazhuang:abcd1234@dynamic.xingsudaili.com:10010',
    #     'https': 'https://dazhuang:abcd1234@dynamic.xingsudaili.com:10010'
    # }

    # response = requests.get(url="http://txt.go.sohu.com/ip/soip",
    #                         proxies=proxy)

    response = requests.get(url="http://txt.go.sohu.com/ip/soip", verify=False)
    ip = re.findall(r'window.sohu_user_ip="(\d+.\d+.\d+.\d+)"',
                    response.text)[0]
    print(response.text, ip, response.status_code)


def taoche():
    url = 'https://m.taocheche.com/cars?city=beijing&storeId=325576'
    response = requests.get(url)
    removeNote = re.sub(r'<!--(.*?)-->', '', response.text)
    nameList = re.findall(
        r'<div class="CarItem_brand.*?">(.*?)</div><div class="CarItem_name.*?">(.*?)</div><div class="CarItem_sub.*?">(.*?)</div>',
        removeNote)
    print(list(nameList))


def beautifulsoup4Test():
    print(
        '=================================beautifulsoup4Test==============================================='
    )
    html = """
         <html>
             <head><title>你好</title></head>
              <body>
                 <p class="content" data-id="属性值">内容 <span class="tag">我是标签</span><span class="tag">我是标签2</span></p></html>
        """
    soup = BeautifulSoup(html, "lxml")  # pip install lxml
    print(soup.title.string)  # 你好
    print(soup.p.attrs)  # {'class': ['content'], 'data-id': '属性值'}
    print(soup.p['class'])  # ['content']
    print(soup.p['data-id'])  # 属性值
    print(soup.head.title.string)  # 你好 # 通过标签名逐层查找
    print(
        soup.p.contents
    )  # ['内容 ', <span class="tag">我是标签</span>, <span class="tag">我是标签2</span>]

    print(soup.p.children)  # <list_iterator object at 0x0000020D3D3D3D30>
    # childList = soup.p.children
    for item in soup.p.children:
        print(item.string)

    # 子孙节点
    for item in soup.p.descendants:
        print(item.string)

    # 父节点
    print(soup.p.parent)
    # 祖先节点
    for item in soup.p.parents:
        print(item)
    # 兄弟节点
    print(soup.p.next_sibling)
    print(soup.p.previous_sibling)
    print(soup.p.next_siblings)
    print(soup.p.previous_siblings)
