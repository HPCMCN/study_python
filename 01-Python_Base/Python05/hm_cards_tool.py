list_card = []


def show_main():
    """展示菜单页面"""
    print("*" * 30, "\n欢迎使用[名片管理系统] V1.0\n\n1.新建名片\n2.显示全部\n3.查询名片\n\n0.退出系统\n", "*" * 30,sep="")
    print("请输入操作指令:")


def new_card():
    """新建名片"""
    print("*" * 10, "新建名片", "*" * 11)
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    qq = input("请输入qq号码:")
    email = input("请输入邮箱:")
    dic_card = {"姓名": name, "电话": phone, "QQ": qq, "邮箱": email}
    list_card.append(dic_card)
    print(name, "信息录入成功!", sep="")


def show_all():
    """展示全部名片"""
    if not len(list_card):  # 如果list_card为0
        print("当前名片为空!")
    else:
        show_table_head()  # 调用表头
        for dic_card in list_card:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (dic_card["姓名"], dic_card["电话"], dic_card["QQ"], dic_card["邮箱"]))
        print("-" * 40)


def find_card():
    """查询名片"""
    if not len(list_card):
        print("当前名片为空!")
    else:
        find_name = input("请输入查询姓名:")
        for dic_card in list_card:
            name = dic_card["姓名"]
            if name == find_name:
                show_table_head()  # 调用表头
                print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (dic_card["姓名"], dic_card["电话"], dic_card["QQ"], dic_card["邮箱"]))
                print("-" * 40)
                deal_card(dic_card)  # 调用处理名片函数
                break
        else:
            print("没有找到%s的相关信息!" % find_name)


def show_table_head():
    """打印表头"""
    print("姓名\t\t\t电话\t\t\tQQ\t\t\t邮箱")
    print("-" * 40)


def deal_card(dic_card):
    """处理名片"""
    while True:
        cmd_num = input("名片操作指令:\n1.修改\n2.删除\n0.返回主菜单")
        if cmd_num == "1":
            dic_card["姓名"] = input("请输入姓名:")
            dic_card["电话"] = input("请输入电话:")
            dic_card["QQ"] = input("请输入QQ:")
            dic_card["邮箱"] = input("请输入邮箱:")
            print("修改成功!")
            break
        elif cmd_num == "2":
            list_card.remove(dic_card)
            print("删除成功!")
            break
        elif cmd_num == "0":
            break
        else:
            print("指令有误,请重试!")
    print("返回主菜单")


