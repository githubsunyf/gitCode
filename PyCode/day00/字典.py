dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 1. [key]
# print(dict1['name'])
# print(dict1['id'])
# 2. get()
# print(dict1.get('name'))
# print(dict1.get('names', 'syf'))
# print(dict1.get('id', 10))
# 3. keys()
print(list(dict1.keys()))
# 4. values()
print(list(dict1.values()))
# 5. items()
print(dict1.items())
for key, value in dict1.items():
    print('key: %s value: %s' % (key, value))

