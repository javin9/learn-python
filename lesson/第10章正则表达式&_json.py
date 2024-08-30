import re


def test():
    str = 'SDD76DS9877wer88654sdfer'

    result = re.match('\d+', str)  # 匹配数字
    print(result.group())

    # result = re.search(r'\d+', str)  # 匹配字母
    # print(result.group())

    text = "The rain in Spain"

    # 使用search()查找是否存在模式"ain"在字符串中
    match = re.search(r"ain", text)
    if match:
        print("找到匹配:", match.group())  # 输出匹配的文本
    else:
        print("没有找到匹配")


def has_number(str):
    result = re.findall(r'\d', str)
    print(result)
    for i in result:
        return True
    return False


# https://www.baidu.com
def trace_url(url):
    result = re.findall(r'[a-zA-Z]{4,5}://\w*\.*\w.\w', url)
    exist = True if len(result) != 0 else False
    print(exist)


def get_url(url):
    result = re.findall(r'[a-zA-Z]{4,5}://(\w*\.*\w+\.\w+)\\?', url)
    if len(result) != 0:
        print(result[0])
        return result[0]
    else:
        return ""


# liujianwei1@tal.com
# liujianwei1213@163.com
def get_email(email):
    result = re.findall(r'\w+@\w+\.[a-zA-Z]+', email)
    exist = True if len(result) != 0 else False
    print(exist)
    return exist


def get_style(html):
    result = re.findall('style="(.*?)"', html)
    if len(result) != 0:
        print(result[0])
        return result[0]


if __name__ == "__main__":
    trace_url("https://www.baidu.com")
    get_url("https://www.baidu.com")
    get_email('liujianwei1213@163.com')
    get_style('<div style="color:red;padding:12px;" class="结果"></div>')
