import urllib.request
import re

def download():
    url = 'http://blog.csdn.net/'

    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    with open('csdn.html','w') as f:
        f.write(data)



if __name__ == '__main__':
    download()