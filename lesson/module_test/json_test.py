import json

str = '{"code":0,"deviceId":"","id":"r1","loginType":"","msg":"","sip":"gk_0_249","uid":""}'

result = json.loads(str)

str2 = json.dumps(result)

print(type(result))

print(type(str2))

s = 'clcoding'
print(s.find('n', 3))
