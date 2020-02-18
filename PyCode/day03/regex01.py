import re

pat = 'yue'
str_data = 'http://yum.iqianyue.com'

res = re.search(pat, str_data)
print(res)
str_data2 ="abdfdsfds"
res = re.search(pat, str_data2)
print(res)