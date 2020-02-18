import re

# 正则 通用字符
# \w 字母数字下划线
# \d 十进制数
# \s 任意一个空白字符

pat = "\w\dpython\w"
str1 = "adfsfdfs"
res = re.search(pat, str1)
print(res)

str2 = "a8pythona"
res = re.search(pat, str2)
print(res)

pat2 = "pyth[abc]n"
str3 = "hellopythonadd"
res = re.search(pat2, str3)
print(res)
str4 = "hellopythanworld"
res = re.search(pat2, str4)
print(res)