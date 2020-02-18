import urllib.request
import urllib.error
import re


data = urllib.request.urlopen("http://news.sina.com.cn/").read()
data2 = data.decode("utf-8", "ignore")
pat = 'href="(http://news.sina.com.cn/.*?)"'
allurl = re.compile(pat).findall(data2)
for i in range(0, len(allurl))
    try:
        print("第"+str(i)+"爬取")
        thisurl = allurl[i]
        file = "news/"+str(i)+".html"
        urllib.request.urlretrieve(thisurl, file)
        print("成功")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)