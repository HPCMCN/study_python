# try:
#     # print(a)
#     a = NameError("name is 'a' not defined")
#     print(id(a))
#     print(a)
#     raise a  # 把异常赋值给error
#
# except NameError as error:
#     print(id(error))
#     print(error)


class CustomException(Exception):  # 创建一个错误类 去继承错误的基类
    pass


phone_num = input("请输入手机号: ")

try:
    if len(phone_num) != 11:
        raise CustomException("手机号码不对")  # 调用错误类  抛出错误类型
    elif phone_num.isdecimal() is False:
        raise CustomException("手机号码不合法")

except CustomException as error:
    print("提示: %s" % error)
