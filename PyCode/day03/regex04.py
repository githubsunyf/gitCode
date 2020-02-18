import re

# . 匹配任意字符
# ^ 匹配字符串开始位置
# & 匹配字符串结束位置
# *
# ? 匹配一次或零次
# + 匹配一次或多次

# {3} 恰好出现3次
# {n,} 至少出现了n次
# {n,m} 至少出现了n次，至多出现了m次
# |
# ()

# pat = 'hello|world'
# str1 = "hello"
# res = re.search(pat, str1)
# print(res)

# 模式修正
# pat = 'python'
# # str1 = "helloPythonworld"
# # res = re.search(pat, str1, re.I)
# # print(res)

# 贪婪模式与懒惰模式
# pat1 = "p.*y"
# pat2 = "p.*?y"   # 懒惰模式
# str1 = "abcdpythonddefadfpy"
# res = re.search(pat2, str1)
# print(res)
# res = re.search(pat1, str1)
# print(res)


# match  从头开始匹配

# compile 全局匹配
# pat1 = 'p.*y'
# # str1 = "hello pdsfdfy world py pddfy"
# # res = re.compile(pat1).findall(str1)
# # print(res)

# 常见正则
