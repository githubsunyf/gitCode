import time

try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            if len(content) == 0
                break
            time.sleep(2)
            print(content)
    except Exception as ex:
        print(ex)
    finally:
        f.close()
except Exception as ex:
    print(ex)