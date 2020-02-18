# 1. 显示功能界面
def info_print():
    print('请选择功能...................')
    print('1. 添加学员')
    print('2. 删除学员')
    print('3. 修改学员')
    print('4. 查询学员')
    print('5. 显示所有学员')
    print('6. 退出系统')
    print('*' * 20)


info = []


def add_info():
    """  添加学员函数 """
    # 1. 用户输入 学号 姓名 手机号
    new_id = input('请输入学号: ')
    new_name = input('请输入姓名: ')
    new_tel = input('请输入手机号: ')

    # 2. 判断姓名是否存在，如果存在报错，如果不存在 添加学员

    global info

    for i in info:
        if new_name == i['name']:
            print('此用户已存在')
            return

    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    info.append(info_dict)
    print(info)


def del_info():
    """ 删除学员 """
    #     用户输入目标学员姓名
    #     检查这个学院是否存在
    global info
    new_name = input('请输入要删除的学员姓名: ')
    for i in info:
        if new_name == i['name']:
            info.remove(i)
            break
        else:
            print('该学员不存在')
    print(info)


def modify_info():
    """修改学员信息"""
    # 1. 用户输入要修改的学员姓名
    # 2. 检查这个学员是否存在
    global info

    modify_name = input('请输入要修改的学员姓名: ')
    modify_tel = input('请输入要修改的手机号: ')
    for i in info:
        if modify_name == i['name']:
            i['tel'] = modify_tel
            break
    else:
        print('该学员不存在!')


def search_info():
    """ 查询学员 """
    search_name = input('请输入要查找的学员姓名: ')
    global info
    for i in info:
        if search_name == i['name']:
            print(i)
            break
    else:
        print('该学员不存在')


def print_all():
    """显示所有学员信息"""
    global info
    for i in info:
        print(f"姓名:{i['name']}, 学号: {i['id']}, 手机: {i['tel']}")


# 2. 用户输入功能序号


# 3. 根据功能序号调用功能函数


while True:

    info_print()
    user_num = int(input('请输入功能序号: '))

    if user_num == 1:
        add_info()
    elif user_num == 2:
        del_info()
    elif user_num == 3:
        modify_info()
    elif user_num == 4:
        search_info()
    elif user_num == 5:
        print_all()
    elif user_num == 6:
        print('退出系统')
    else:
        print('输入的功能序号有误')
