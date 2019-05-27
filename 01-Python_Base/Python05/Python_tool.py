# 登陆系统ool  注册系统tool     注销系统tool  创建字典tool
# 注册系统


def register(list1):
    """注册系统"""
    print("*" * 15, "注册", "*" * 16)
    while True:
        while True:
            name1 = input("请输入用户名\n")
            if len(name1) in range(6, 21) and name1.isdecimal() == 0:  # 当 name1总数在[6, 21)中且不是纯数字条件通过
                for name in list1:
                    if name1 in name["用户名"]:  # 创建函数  去搜索字典中是否存在相同的数据
                        print("用户已存在!")
                        break
                else:
                    break
            else:
                print("格式错误!用户名必须有6~20个字符组成,且不能纯数字.")
        while True:
            pwd = input("请输入密码:\n")
            if len(pwd) in range(8, 21) and pwd.isdecimal() == 0:
                set1 = []
                for name in pwd:  # 用set处理重复字符串,若字符串总数是1 说明字符串重复
                    set1.append(name)
                if len(set(set1)) == 1:
                    print("格式错误!密码必须有8~20个字符组成,且不能重复.")
                else:
                    break
            else:
                print("格式错误!密码必须有8~20个字符组成,不能纯数字.")
        nickname = input("请输入昵称:\n")
        while True:
            age = input("请输入年龄:\n")
            if age.isdecimal() and (int(age) in range(18, 130)):
                break
            else:
                print("年龄必须在18~130之间的纯数字")
        user_message = {"用户名": name1, "密码": pwd, "昵称": nickname, "年龄": age}
        list1.append(user_message)
        print("注册成功,请登陆!")
        return


def login(list1, i=0):
    """登陆系统"""
    print("*" * 15, "登陆", "*" * 16)
    while True:
        name1 = input("用户名:")
        pwd = input("密码:")
        if len(list1) != 0:
            for name in list1:
                if i < 4:
                    if name1 in name["用户名"]:  # 创建函数  去搜索字典中是否存在相同的数据
                        if name["密码"] == pwd:
                            i = 5
                            print("登陆成功!")
                            print("%s欢迎归来" % name["用户名"])
                            i = os(i)
                            break
                        else:
                            print("密码错误,还有%d次机会!请注意大小写!" % (3-i))
                            i += 1
                            break
                elif i == 5:
                    print("登陆失败,用户已登陆!")
                    break
                else:
                    print("已超出上限,请稍后重试!")
                    break
            else:
                print("用户名不存在,请核实后再试!")
                while True:
                    cmd_1 = input("1.继续\n2.退出")
                    if int(cmd_1) in [1, 2]:
                        break
                    else:
                        print("指令有误!")
                if cmd_1 == "1":
                    continue
                else:
                    break
        else:
            print("用户名不存在,请核实后再试!")
            while True:
                cmd_1 = input("1.继续\n2.退出")
                if int(cmd_1) in [1, 2]:
                    break
                else:
                    print("指令有误!")
            if cmd_1 == "1":
                continue
            else:
                break
        if i == 5 or i == 3:
            break
    return i


def os(a):
    """操作系统"""
    print("*" * 15, "登陆", "*" * 16)
    print("模块为空,正在填加")
    while True:
        m = input("1.返回主菜单0.注销")
        if m == "1":
            print("正在返回主菜单...")
            break
        elif m == "0":
            print("正在注销...")
            a = 0
            print("已注销")
            break
        else:
            print("指令有误!")
    return a
