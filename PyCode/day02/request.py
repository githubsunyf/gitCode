
import urllib.request

def load_baidu():
    url = "http://www.baidu.com"

    header = {
        # 浏览器基本信息
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    # request.get_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode('utf-8')

    # 获取完整的url
    final_url = request.get_full_url()

    #响应头
    #print(response.headers)

    #获取响应头的信息
    # request_header = request.headers

    request_header = request.get_header('User-agent')
    print(request_header)
    with open("02header.html", "w", encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    load_baidu()

