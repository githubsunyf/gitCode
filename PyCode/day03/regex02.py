import re

pat = "\n"
str1 = """hello
world"""
res = re.search(pat, str1)
print(res)