import urllib.request
import random


def proxy_user():
    proxy_list = [
        {"http": "123.149.141.46:9999"},
        {"http": "123.169.37.242:9999"},
        {"http:" "114.99.0.48:9999"},
        {"http": "182.35.86.125:9999"},
        {"http": "182.108.60.15:9999"}
    ]

    proxy = random.choice(proxy_list)
    # 利用遍历出来的ip创建处理器

    httpproxy_handler = urllib.request.ProxyHandler(proxy)
    # 创建opener
    opener = urllib.request.build_opener(httpproxy_handler)

    # opener = urllib.request.build_opener(proxy_handler)

    try:
        # opener.open("http://www.baidu.com", timeout=1)
        response = opener.open("http://www.baidu.com")
        print(response.read().decode('utf-8'))
    except Exception as e:
        print(e)


proxy_user()
