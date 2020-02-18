# 响应类型
import urllib.open
response = urllib.request.urlopen('https:///www.python.org')
print(type(response))
# 状态码， 响应头
import urllib.request
response = urllib.request.urlopen('https://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))