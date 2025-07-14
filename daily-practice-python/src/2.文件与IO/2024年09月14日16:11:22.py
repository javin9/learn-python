# import pickle

# # 序列化对象
# data = {'name': 'Alice', 'age': 30, 'is_employee': True}
# with open('data.pkl', 'wb') as file:
#     pickle.dump(data, file)

# # 反序列化对象
# with open('data.pkl', 'rb') as file:
#     loaded_data = pickle.load(file)
# print(loaded_data)
import json
from collections import OrderedDict

s = '{ "shares": 50,"name": "ACME", "price": 490.1}'
data = json.loads(s, object_hook=OrderedDict)
print(data)
