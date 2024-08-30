import requests
import re


class Spider:

    # url = 'https://top.baidu.com/board?tab=novel'

    def __init__(self, name):
        self.name = name

    def crawl(self, url):
        print(f'{self.name} is crawling {url}')
        response = requests.get(url)
        # print(response)
        if response.status_code == 200:
            # print(response.text)
            html_content = response.text

            str = re.sub(r'<!--(.*?)-->', '',
                         html_content)  # .replace(" ", "")
            str = re.sub(r'\n', '', str)
            # print(str)

            with open("./index.html", 'a') as f:
                f.write(str)

            # nameList = re.findall(
            #     r'<div class="c-single-text-ellipsis">(.*?)</div>',
            #     html_content)

            info = re.findall(
                r'<div class="content_1YWBm"> <a href="(.*?)" class="title_dIF3B " target="_blank"> <div class="c-single-text-ellipsis">  (.*?) </div>  </a>  <div class="intro_1l0wp"> (.*?) </div><div class="intro_1l0wp"> (.*?) </div> <div class="c-single-text-ellipsis desc_3CTjT"> (.*?) <a href="(.*?)" class="look-more_3oNWC" target="_blank"> 查看更多&gt; </a> </div>',
                str)

            # print(nameList)
            print(info)
            # with open("./data.py", 'a') as f:
            #     f.write("---------------".join(info))
