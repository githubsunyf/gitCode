import urllib.request
import re

url = "http://blog.csdn.net/"

# 伪装

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request)
# print(response)
# data = response.read().decode('utf-8')
# print(data)


# 方式二
headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode('utf-8',"ignore")
pat = '<h2>\s*<a href="(.*?)"'
allurl = re.compile(pat).findall(data)
for i in range(0,len(allurl)):
    file = "csdn/result/"+str(i)+".html"
    urllib.request.urlretrieve(allurl[i], filename=file)
    print('第'+str(i)+"次爬取成功")
print(allurl)
