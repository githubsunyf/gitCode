import urllib.request
import urllib.parse

# 表单登陆模拟

url = ""

mydata = urllib.parse.urlencode({
    "name":"zhangsan",
    "pass":"123456"
}).encode('utf-8')

req = urllib.request.Request(url, mydata)

# 伪装浏览器
# req.add_header("")
res = urllib.request.urlopen(req).read()
f = open("open.html", "wb")
f.write(res)
f.close()


