
""" 当一个类有多个父类的时候，默认使用的第一个父类的同名属性和方法 """
""" 子类和父类具有同名属性和方法，默认使用子类的同名属性和方法 """

class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


class B(object):
    def __init__(self):
        self.num = 2

    def info_print(self):
        print(self.num)


class C(A, B):
    def info_print(self):
        print('hello')


result = C()
result.info_print()
print(C.__mro__)



