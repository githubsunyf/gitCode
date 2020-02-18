import urllib.request

def auth_nei_wang():
    # 1.用户名密码
    user = "admin"
    pwd = "adminn123"
    nei_url = "http://192.168.179.66"

    # 2. 创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()

    pwd_manager.add_password(None, nei_url, user, pwd)

    # 创建认证处理器
    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)

    # 创建opener
    opener = urllib.request.build_opener(auth_handler)
    res = opener.open(nei_url)
    print(res.read().decode('utf-8'))


