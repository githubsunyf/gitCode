import functools


def fn1():
    return 200


print(fn1)

fn2 = lambda : 100

print(fn2)
print(fn2())

fn3 = lambda a, b : a + b
print(fn3(2, 4))

# 一个参数
fn4 = lambda a : a
print(fn4('hello lambda'))

# 默认参数
fn5 = lambda a, b, c=100 : a + b + c
print(fn5(1, 2))

# 可变参数
fn6 = lambda *args: args
print(fn6(1, 2, 3, 4))

# 可变参数 **kwargs
fn7 = lambda **kwargs : kwargs
print(fn7(name='python', age=20))


# 高阶函数

def sum_num(a, b, f):
    return f(a) + f(b)

result = sum_num(-1, 2, abs)

# 内置高阶函数
# map(func,list) 将传入的函数变量func作用到list变量的每个元素中，并将结果组成新的列表
list1 = [1, 2, 3, 4]

def func(x):
    return x ** 2
result1 = map(func, list1)
print(list(result1))

# reduce(func,list) 其中func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累积计算

list2 = [2, 4, 5, 7]

def func2(a, b):
    return a + b

result3 = functools.reduce(func2,list2)
print(result3)

# filter(func,list) 函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，如果要转化为列表，可以用list()来转换

list3 = range(0, 20, 2)
def func3(x):
    return x % 2 == 0

result4 = filter(func3, list3)
print(list(result4))