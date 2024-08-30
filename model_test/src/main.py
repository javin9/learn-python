import requests

print("hello model")

result = requests.get("http://www.baidu.com")
print(result.status_code)
