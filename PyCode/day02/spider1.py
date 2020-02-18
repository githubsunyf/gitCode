import urllib.request

def load_data():
    url = 'http://www.baidu.com/'

    # get请求
    response = urllib.request.urlopen(url)
    print(response)
    # 读取内容 bytes类型
    data = response.read()
    print(data)
    # 将文件获取的内容转汉城字符串
    str_data = data.decode('utf-8')
    print(str_data)
    with open('../baidu.html', 'w', encoding='utf-8') as f:
        f.write(str_data)


if __name__ == '__main__':
    load_data()

