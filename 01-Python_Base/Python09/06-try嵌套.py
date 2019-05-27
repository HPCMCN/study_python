try:
    f = open("123.txt", "r")
    try:
        print(a)
        content = f.read()
        print(content)
        f.close()
    except FileNotFoundError as error1:
        print("错误: %s" % error1)
except BaseException as error:
    print("提示: %s" % error)


print("只要能拦住就输出本行代码")
