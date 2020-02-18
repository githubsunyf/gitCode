import urllib.request
import urllib.parse
import string

def load_data():
    # 目标地址
    url = 'http://www.baidu.com/s?wd='

    name = '美女'
    final_url = url + name
    print(final_url)
    # 将包含汉字的网址进行转义
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_new_url)
    response = urllib.request.urlopen(encode_new_url)
    data = response.read()


if __name__ == '__main__':
    load_data()

