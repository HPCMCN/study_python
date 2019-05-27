import os
# company = input("请输入公司名称:\n")
# name = input("请输入名字:\n")
# title = input("请输入职务:\n")
# telephone = input("请输入电话:\n")
# email = input("请输入邮箱:\n")
# print("*" * 50)
# print("公司名称:\n%s\n姓名(职位)\n%s(%s)\n电话:%s\n邮箱:%s" % (company, name, title, telephone, email))
# print("*" * 50)


# """
# 在控制台依次提示⽤户输⼊：姓名、公司、职位、电话、电⼦邮箱
# """
# name = input("请输⼊姓名：")
# company = input("请输⼊公司：")
# title = input("请输⼊职位：")
# phone = input("请输⼊电话：")
# email = input("请输⼊邮箱：")
# print("*" * 50)
# print(company)
# print()
# print("%s (%s)" % (name, title))
# print()
# print("电话：%s" % phone)
# print("邮箱：%s" % email)
# print("*" * 50)

# def jiujiu():
#     """九九乘法表"""
#     for i in range(1, 10):
#         print()
#         for x in range(1, 10):
#             if x <= i:
#                 print("%d * %d = %d\t" % (x, i, x * i), end="")
#
#
# jiujiu()

"""九九乘法表"""


def open_file():
    """未知函数"""
    a = os.getcwd()
    print(a)
    with open("filename.txt.py", "r") as f:
        while True:
            content = f.readline()
            print(content, end="")
            if content is None:
                break


open_file()
