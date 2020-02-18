try:
    print(1)
except Exception as result:
    print(result)
else:
    print('一切正常')
finally:
    print('执行结束')