def new_card(list1):
    """新建名片"""
    print("功能: 新建名片")
    # 获取用户信息添加到字典中 并把字典添加到列表中
    name_str = input("请输入姓名:")
    phone_num = input("请输入电话:")
    qq_num = input("请输入QQ:")
    mail_adr = input("请输入邮箱:")
    card_info = {"name": name_str, "phone_num": phone_num, "qq_num": qq_num, "mail_adr": mail_adr}
    list1.append(card_info)
    print("添加%s的名片成功" % name_str)


def show_all(list1):
    """展示所有字典"""
    print("功能:展示全部")
    if len(list1) == 0:
        print("名片记录为空")
    else:
        print("姓名\t\t电话\t\tqq\t\t邮箱")
        print("*" * 30)
        for card_info in list1:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_info["name"], card_info["phone_num"], card_info["qq_num"],
                                            card_info["mail_adr"]))
        print("*" * 30)


def find_name(list1):
    """查找名字"""
    print("功能:查找名片")
    cmd_find = input("请输入名字:")
    for card_info in list1:
        if card_info["name"] == cmd_find:
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("*" * 30)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_info["name"], card_info["phone_num"], card_info["qq_num"],
                                            card_info["mail_adr"]))
            print("*" * 30)
            deal_card(card_info)
            break
    else:
        print("没有找到")


def deal_card(card_info):
    """处理名片"""
    while True:
        cmd_num = input("请输入对名片的操作:1.修改/2.删除/0.返回上一级")
        if cmd_num == "1":
            print("修改名片")
            update_card(card_info)
            break
        elif cmd_num == "2":
            print("删除名片")
            break
        elif cmd_num == "0":
            break
        else:
            print("指令有误")


def update_card(card_info):
    """修改名片"""
    card_info["name"] = input("请输入姓名:")
    card_info["phone_num"] = input("请输入电话:")
    card_info["qq_num"] = input("请输入qq:")
    card_info["mail_adr"] = input("请输入邮箱:")
    print("%s 的名片修改成功" % card_info["name"])
