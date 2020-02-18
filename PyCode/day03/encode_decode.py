'''

encode和decode分别指编码和解码
在 python中， Unicode类型是作为编码的基础类型，即
str --->  str(Unicode) ---> str
'''

str_data = '你好中国！hello，123'

str1 = str_data.encode('gb2312')
print(str1)

str2 = str_data.encode('gbk')
print(str2)

str3 = str_data.encode('utf-8')
print(str3)

str1_1 = str1.decode('gb2312')
print(str1_1)

str2_1 = str2.decode('gbk')
print(str2_1)

str3_1 = str3.decode('utf-8')
print(str3_1)