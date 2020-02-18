import urllib.request



def create_proxy_handler():
    url = "https://www.csdn.net/"

    # 添加代理
    proxy = {
        "http": "http://123.149.141.46:9999"
    }

    #代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    #创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)

    data = opener.open(url).read()
    print(data)


create_proxy_handler()