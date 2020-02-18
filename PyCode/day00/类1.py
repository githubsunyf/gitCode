

class Washer():
    def __init__(self):
        print('在创建一个对象时默认被调用，不需要手动调用/ 构造函数')

    def __str__(self):
        return '这是洗衣机的说明书'
    # 当使用print输出对象的时候，默认打印对象的内存地址，如果类定义了__str__方法，那么就会从在这个方法中return的数据

    def __del__(self):
        # 当删除对象时，python解释器也会默认调用__del__()方法
        print('删除对象中。。。')

    def wash(self):
        print('洗衣服')
        print(f'洗衣机的宽度{self.width}')
        print(f'洗衣机的高度{self.height}')



w = Washer()


w.width = 200
w.height = 300

w.wash()