# 主控制中心
import Python_tool
list1 = []
print(" " * 8, "职员信息管理系统 V2.0")
a = 0
while True:
    print("*" * 15, "主菜单", "*" * 16)
    cmd_num = input("请输入你的操作: \n1.登陆系统 \n2.注册系统 \n\n\n0.退出系统\n")
    if cmd_num == "1":
        print("正在进入登陆系统...")
        a = Python_tool.login(list1, a)
    elif cmd_num == "2":
        print("正在进入注册系统...")
        Python_tool.register(list1)
    elif cmd_num == "0":
        print("正在退出,请稍后...")
        break
    else:
        print("指令有误!")
