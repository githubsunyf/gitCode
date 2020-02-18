import  urllib.request

def handler_openner():
    #系统的urlopen并没有添加代理的功能 所以需要我们自定义这个功能

    # urllib.request.urlopen()
    url = "https://www.csdn.net/"
    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的openner
    opener = urllib.request.build_opener(handler)
    #用自己创建的openner调用open方法请求数据
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)



handler_openner()








