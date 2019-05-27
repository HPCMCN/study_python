# 主函数
import 练习.ming_pian_tool
list1 = []
while True:  # 创建一个死循环 用来做显示页面
    # 获取用户输入信息进行判断
    print("*" * 30)
    print("欢迎使用[名片管理系统] V1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 30)
    cmd_num = input("请选择执行的操作")
    print("你选择的操作是%s" % cmd_num)
    if cmd_num == "1":
        print("新建名片")
        练习.ming_pian_tool.new_card(list1)
    elif cmd_num == "2":
        print("显示全部")
        练习.ming_pian_tool.show_all(list1)
    elif cmd_num == "3":
        print("查询名片")
        练习.ming_pian_tool.find_name(list1)
    elif cmd_num == "4":
        print("欢迎再次使用[名片管理系统]")
        break
    elif cmd_num == "0":
        break
    else:
        print("输入有误,请重试!")
