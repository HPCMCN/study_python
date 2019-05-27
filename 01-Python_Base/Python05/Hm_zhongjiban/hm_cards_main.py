import hm_cards_tool
hm_cards_tool.read_card()
while True:
    hm_cards_tool.show_main()   # 展示主菜单
    cmd_num = input()
    print("当前操作:", end="")  # 显示当前操作
    if cmd_num == "1":
        print("新建名片")
        hm_cards_tool.new_card()  # 调用新建名片函数
    elif cmd_num == "2":
        print("显示全部", sep="")
        hm_cards_tool.show_all()  # 调用显示全部函数
    elif cmd_num == "3":
        print("查询名片")
        hm_cards_tool.find_card()  # 调用查找姓名函数
    elif cmd_num == "4":
        print("保存名片")
        hm_cards_tool.writer_card()
    elif cmd_num == "0":
        print("退出系统")
        break
    else:
        print("指令有误,请核实后重试!")
        print(cmd_num)
