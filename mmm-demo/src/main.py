import requests

print("hello world")

# 百度首页URL
url = "https://www.baidu.com"

# 发送GET请求
response = requests.get(url)

# 打印响应状态码
print(f"Response Status Code: {response.status_code}")

# 打印响应内容（前500个字符）
print(response.text[:500])
