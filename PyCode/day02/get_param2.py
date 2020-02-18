import urllib.request
import urllib.parse
import string

def load_data():
    url = 'http://www.baidu.com/s?'
    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"san"
    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params
    # 将带有中文的url 进行转义
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(end_url)
    data = response.read().decode('utf-8')
    with open('../2.html', 'w', encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    load_data()