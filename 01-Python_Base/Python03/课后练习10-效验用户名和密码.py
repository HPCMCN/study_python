"""
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印出字符串长度
使用切片逆序打印出字符串
"""
# while True:
#     str1 = input("请输入一个低于31的字符串:\n")
#     if len(str1) > 31:
#         print("请重新输入一个低于31的字符串!")
#         continue
#     else:
#         print("字符串的长度是:%d\n" % len(str1))
#         print("字符串倒序为:%s" % str1[::-1])
#         break

"""
要求从键盘输入用户名和密码，校验格式是否符合规则，如果不符合，打印出不符合的原因，并提示重新输入
用户名长度6-20，用户名必须以字母开头not 6 <= len(names) <= 20 or
密码长度至少6位，不能为纯数字，不能有空格
"""


def efficacy():
    while True:
        names = input("退出直接回车\n请输入用户名:\n")
        if names == "":
            break
        if not names[0].isalpha() or not 6 <= len(names) <= 20:
            print("用户名格式不正确,长度6-20，用户名必须以字母开头")
            continue
        pwd = input("请输入密码:\n")
        i = 0
        while i < len(pwd):
            name = pwd[i]
            i += 1
            if name == " ":
                i = -1
                break
        if len(pwd) < 6 or i == -1 or pwd.isdecimal():
            print("密码长度至少6位，不能为纯数字，不能有空格")
        if names == "BSODGM" and pwd == "w123456":
            print("登陆成功!")
            break
        else:
            print("登陆失败!")


efficacy()

