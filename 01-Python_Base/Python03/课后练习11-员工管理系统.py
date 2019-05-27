"""
字典和列表的不同以及使用字典的目的
字典是由键值构成,无序的,可以由键值成对存在,且键不能重复 列表是元素  有序的  每个元素能重复
怎样创建一个空字典
dic = {}
怎样向字典中添加新的key-value
dic["key"] = "value"
怎样访问字典中元素
name = dic["元素"]
怎样修改字典中的元素
dic["name"] = "想修改的内容"
删除某个元素
del dic[想删除的元素]
删除整个字典
del dic
清空整个字典
dic.clear
怎样测量键值对个数
len(dic)
怎样获取字典中所有的key
import sys
keys = dic.keys()
print(keys)
怎样获取字典中所有的value
import sys
value = dic.values()
print(value)
怎样用for循环变量字典
import sys
items = dic.items()
for key, value in dic.items():
    print(key)
    print(value)
编程：使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），这些信息来自 键盘的输入
"""
# print("个人信息登记\n")
# dict1 = {}
# while True:
#     name = input("请输入:\n1.姓名\n2.年龄\n3.学号\n4.QQ\n5.微信\n6.住址\n0.任意键退出")
#     if name == "1":
#         name = input("请输入姓名:\n")
#         dict1["姓名"] = name
#     elif name == "2":
#         age = input("请输入年龄:\n")
#         dict1["年龄"] = age
#     elif name == "3":
#         student_num = input("请输入学号:\n")
#         dict1["学号"] = student_num
#     elif name == "4":
#         QQ = input("请输入QQ:\n")
#         dict1["QQ"] = QQ
#     elif name == "5":
#         char = input("请输入微信:\n")
#         dict1["微信"] = char
#     elif name == "6":
#         where = input("请输入住址:\n")
#         dict1["住址"] = where
#     else:
#         print("正在关闭!......")
#         break
#
# print("*" * 20)
# import sys
# item = dict1.items()
# for key, value in item:
#     print("%s:%s" % (key, value))
# print("*" * 20)


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
# list1 = []
# while True:
#     dic1 = {}
#     str1 = input("请输入一个低于31的字符串:\n")
#     if len(str1) > 31:
#         print("请重新输入一个低于31的字符串!")
#         continue
#     else:
#         if str1 == "" or str1[:2] == "查询":
#             break
#         else:
#             print("字符串的长度是:%d\n" % len(str1))
#             print("字符串倒序为:%s" % str1[::-1])
#             dic1["原字符串"] = str1
#             dic1["长度"] = len(str1)
#             dic1["倒序"] = str1[::-1]
#             # print(list1)
#             list1.append(dic1)
#             # print(list1)
#             del dic1
#             # print(list1)
# if str1[:2] == "查询":
#     i = 0
#     for name in list1[i]:
#         if str1[2:] == list1[i][name]:
#             print(list1[i])
#             break
#     else:
#         print("没有找到!")
#         i += 1
# else:
#     print(list1)


"""
查看笔记本键盘1-9还有0号键其上方的字符，要求用户输入"1"，那么输出"!",输入"2"，那么输出"@",以此类推
用字典完成这个任务
用户如果输入的字符长度超过1或者是除数字以外其他字符，提示"未收录该字符的含义，请重新输入"
"""

# dict1 = {
#     "1": "!",
#     "2": "@",
#     "3": "#",
#     "4": "$",
#     "5": "%",
#     "6": "^",
#     "7": "&",
#     "8": "*",
#     "9": "(",
#     "0": ")",
#     "`": "~",
#     "-": "_",
#     "=": "+"
# }
# while True:
#     input1 = input("请输入需要转换的字符:")
#     if input1 == "":
#         break
#     elif input1 in dict1:
#         print(dict1[input1])
#     else:
#         print("没有收录该定义字符!请重试.....")

"""
要求依次从键盘录入每位员工的信息，包括姓名、员工id、出生年月、籍贯、身份证号、入职时间
身份证号十八位，要求除了第18位可以为x，其余都只能为数字
id须由数字组成
否则提示用户重新输入不符合规则的那几项
要求能随时查看已录入的员工及其信息
"""
print("员工管理系统")


def eid(name5, list1):
    """修改模块"""
    name1 = input("修改对应如下,退出直接回车:\n1.姓名\n2.员工id\n3.出生年月\n4.籍贯\n5.身份证号\n6.入职时间\n\n\n\n0.键入其他键继续查找\n")
    if name1 == "1":
        name2 = input_name()
        name5["姓名"] = name2  # 修改名字
    elif name1 == "2":
        while True:
            m, name2 = input_id(list1)
            if name2 == "":
                break
            elif m == 1:
                name5["员工id"] = name2
                break
    elif name1 == "3":
        name2 = input_birthday()
        name5["出生年月"] = name2
    elif name1 == "4":
        name2 = input_np()
        name5["籍贯"] = name2
    elif name1 == "5":
        while True:
            m, name2 = input_card(list1)
            if m == 1:
                name5["身份证"] = name2
                break
            elif name2 == "":
                break
    elif name1 == "6":
        name2 = input_time()
        name5["入职时间"] = name2
    else:
        print("输入指令有误,请重试!")
    return list1



def find1(list1, names, x=0):
    """查找信息模块"""
    i = 0
    n = 0
    if len(list1) != 0:
        for name5 in list1:
            for name in name5:
                if name5[name] == names:
                    n = -1
                    if x == 0:  # x == 0 表示查询
                        print(name)
                        print(list1[i])
                    elif x == -2:  # x == -2  表示效验是否重复
                        break
                    if x == -1:  # 如果x = -1,本次循环结束,可以进行修改
                        break
            i += 1
            if x == -1 and n == -1:
                i -= 1
                list1 = eid(name5, list1)
                print("修改完成!")
                break
            elif x == -2:
                if n == -1:
                    print("该信息已存在!", end="")
                    return n
                else:
                    return n
        if n == 0:
            print("查找内容不存在!请录入后再试!")
    elif x == -2:
        return n
    else:
        print("本名片位空,请录入后重试!")
    return list1, n


def add1(m):   #m = -1程序结束   m = -2查找  m = -3修改
    """信息录入判断模块"""
    m += 1
    names = input()
    if names == "":
        m = -1
    elif names == "2":
        m = -2
    elif names == "3":
        m = -4
    elif names == "1":
        m = m
    else:
        m = -3
        print("指令错误,重新输入!")
    return m, names


def print_input():
    """打印提示用户"""
    print("*" * 10, "主菜单", "*" * 10)
    print("1.录入模块\n2.查询模块\n3.修改模块")


def input_name():
    names = input("请输入名字:\n")
    return names


def input_birthday():
    names = input("请输入出生日期:\n")
    return names


def input_np():
    names = input("请输入籍贯:\n")
    return names


def input_time():
    names = input("请输入入职时间:\n")
    return names


def input_id(list1):
    """判断并导入员工id"""
    names = input("请输入员工id:\n")
    x = -2
    n = find1(list1, names, x)
    if names.isdecimal() and n != -1:
        m = 1
    else:
        m = 0
        print("请重新输入id,必须纯数字!")
    return m, names


def input_card(list1):
    """判断并导入身份证信息"""
    names = input("请输入身份证:\n")
    x = -2
    n = find1(list1, names, x)
    if (names[:-1].isdecimal() and (names[-1:].isdecimal() or (names[-1:] == "X"))) and (len(names) == 18) and n != -1:
        m = 1
    else:
        print("请重新输入身份证,必须18位且除最后一位可以用X外,需要纯数字")
        m = 0
    return m, names


def sense1(m, dict1):
    """信息录入模块"""
    if m == 1:
        print("*" * 10, "录入模块", "*" * 10)
        names = input_name()
        dict1["姓名"] = names
    elif m == 2:
        while True:
            m, names = input_id(list1)
            if names == "":
                break
            elif m == 1:
                dict1["员工id"] = names
                break

    elif m == 3:
        names = input_birthday()
        dict1["出生年月"] = names
    elif m == 4:
        names = input_np()
        dict1["籍贯"] = names
    elif m == 5:
        while True:
            m, names = input_card(list1)
            if m == 1:
                dict1["身份证"] = names
                break
            elif names == "":
                break
    elif m == 6:
        names = input_time()
        dict1["入职时间"] = names
    return dict1


a = 0
list1 = []
while True:
    dict1 = {}
    m = 0
    print_input()
    m, names = add1(m)  # 返回m = -1程序结束   m = -2查找  正常运行返回0
    while True:  # m, a, names
        if m == -1 or m == -3:
            print("正在退出程序!")
            break
        elif m == -2:
            print("*" * 10, "查找模块", "*" * 10)
            names = input("请输入查找内容:\n")
            if names == "":
                break
            else:
                list1 = find1(list1, names)
        elif m == -4:
            print("*" * 10, "修改模块", "*" * 10)
            names = input("请输入修改用户")
            x = -1
            if names == "":
                break
            else:
                list1 = find1(list1, names, x)
        elif m <= 6:
           dict1 = sense1(m, dict1)  # 在此处加一个变量 用来判定是否信息录入成功
           m += 1
        else:
            break
    if len(dict1) != 0:
        list1.append(dict1)
        print("录入成功", end="")
    if m == -1:
        break
    else:
        print("返回主菜单!")
print("本系统名单如下:")
print(list1)

