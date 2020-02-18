import urllib.request

keywd = 'python'

url = "http://www.baidu.com/s?wd="+keywd
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
f = open("python.html", "wb")
f.write(res.read())
f.close()