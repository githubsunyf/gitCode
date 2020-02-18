

# bytes object
b = b'example'

# str object
s = 'example'

# str to bytes
print(bytes(s, encoding='utf-8'))

# bytes to str
print(str(b, encoding='utf-8'))

# an alternative method
# str to bytes
print(str.encode(s, encoding='utf-8'))

# bytes to str
print(bytes.decode(b, encoding='utf-8'))
