# 简单例子
import urllib.request
request = urllib.request.Requests('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

# 增加header
from urllib import request, parse
url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    'Host':'httpbin.org'
}
# 构造POST表格
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read()).decode('utf-8')