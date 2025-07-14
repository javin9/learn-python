data = {"name": "Alice", "age": 20, "city": "Beijing"}

for key, value in data.items():
    print(key, value)

print("-" * 10)
for key in data.keys():
    print(key)

print("-" * 10)
for value in data.values():
    print(value)
