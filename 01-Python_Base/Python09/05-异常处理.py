try:  # 专门用来测试代码是不是有错误的
    f = open("123.txt", "r")
    content = f.read()
    print(content)
    f.close()
    print(A)

# except:  #所有异常都能拦截   但是不能看到异常的信息
#     print("xxxx")
except FileExistsError as error:
    print(error)
except Exception as error:  # 为所有错误代码的基类
    print(error)
except BaseException as error:  # 为Exception 的基类
    print(error)
else:
    print("当try里面没有出错时, 就会执行else中的代码")
finally:
    print("没有啥作用, 不管有没有错都会执行")


print("只要能拦截就会执行本代码")