"""
python中字符串的组成及表示规则是怎样的
各种引号  文本类型数据
如何理解下标，怎么使用下标来获取字符串中的某个字符
字符串每个分隔的位置   print(字符串(下标))
如何理解切片，怎么使用切片来获取字符串中的一些字符
分割字符串, 字符串[起始位置:结束位置]
怎样判断一个变量是否是字符串类型
print(type(变量))
怎样使用print输出一个字符串
print("字符串")
怎样测得字符的长
print(len(字符串))
有"100"和100，它们有什么区别么？
一个是string.一个是int
怎样将"100"转换为100
int("100")
怎样将100转换为"100"

编程题：从键盘输入一个用户名和密码，判断是否正确，如果是则打印登录系统成功，否则显示用户名或密码错误
"""
# str ="123"
# num = int()
# str1 = """100"""
# # char = str1[1]
# print(type(str1))
# i = 0
# while True:
#     name = input("请输入用户名:\n")
#     pwd = input("请输入密码:\n")
#     dict1 = {
#         "name": "小明",
#         "psd": "111111"
#     }
#     if name != dict1["name"]:
#         print("用户名不存在!")
#         i += 1
#     else:
#         if pwd == dict1["psd"]:
#             print("登陆成功!")
#             break
#         else:
#             print("密码错误!")
#             i += 1
#     if i >= 3:
#         print("不要暴力破解!")
#         break


"""
名片管理器v1.0

控制姓名长度为6-20
电话号码长度11
性别只能允许输入男或女
每一样信息不允许为空
"""
# print("名片管理器v1.0")
# name = input("请输入名字:\n")
# tel = input("请输入电话:\n")
# sex = input("请输入性别:\n")
# card1 ={}
# i = 0
# if 6 <= len(name) <= 20:
#     i += 1
# elif len(name) == 0:
#     print("名字不能为空!")
# else:
#     print("名字不在控制范围内!")
# if len(tel) == 11:
#     i += 1
# elif len(tel) == 0:
#     print("电话不能为空!")
# else:
#     print("电话号码输入错误!")
# if sex == "男" or "女":
#     i += 1
# elif len(sex) == 0:
#     print("性别不能为空!")
# else:
#     print("不接受其他性别")
# if i == 3:
#     print("录入成功!")
#     card1["name"] = name
#     card1["tel"] = tel
#     card1["sex"] = sex
#     print(card1)
# else:
#     print("手动自启程序吧!")

"""
名片管理器v2.0
在上一版本的基础上，增加可以添加多个名片的功能
可以打印所有名片的功能
可以删除名片的功能
"""
print("名片管理器v2.0")
#   已经完成
card1 = []
card2 = []
card3 = []
while True:
    tel = []
    sex = []
    i = 0
    name = input("请输入相关指令:\n1.添加名片(直接输入名字)\n2.查找+名字\n3.删除+名字\n4.修改+名字\n5.退出直接回车\n")
    if name == "":
        break
    elif "删除" == name[:2]:
        name = name[2:]
        num = card1.index(name)
        del card1[num]
        del card2[num]
        del card3[num]
        print("已经删除%s的相关信息!" % name)
    elif "查找" == name[:2] or "查询" == name[:2]:
        name = name[2:]
        if name not in card1:
            print("查找失败,没有此人!")
        else:
            num = card1.index(name)
            num1 = card1[num]
            num2 = card2[num]
            num3 = card3[num]
            print("name: %s\ntel: %s\nsex: %s" % (num1, num2, num3))
    else:
        if "修改" == name[:2]:
            name = name[2:]
            if name[2:] == "姓名" or "名字":
                name = name[2:]
                if "电话" == name[-2:]:
                    name = name[:-2]
                    tel1 = card1.index(name)
                    tel = input("请输入修改的电话:\n")
                    name = []
                    i = 5
                elif "性别" == name[-2:]:
                    name = name[:-2]
                    sex1 = card1.index(name)
                    sex = input("请输入修改的性别:\n")
                    name = []
                    i = 6
                else:
                    name1 = card1.index(name)
                    name = input("请输入修改的名字:\n")
                    i = 3
        else:
            tel = input("请输入电话:\n")
            sex = input("请输入性别:\n")
        if 6 <= len(name) <= 20:
            i += 1
            if i > 3:
                print("正在修改.", end="")
        elif i > 3:
                print("正在修改.", end="")
        elif len(name) == 0:
            print("名字不能为空!")
        else:
            print("名字不在控制范围内!")
            i = 0
        if len(tel) == 11:
            i += 1
        elif i > 3:
            print("..", end="")
        else:
            print("电话号码输入错误,请检查是否为空或输入格式有误!")
            i = 0
        if "男" == sex or "女" == sex:
            i += 1
        elif i > 3:
            print("..")
        else:
            print("不接受其他性别")
            i = 0
        if i == 3:
            print("录入成功!")
            card1.append(name)
            card2.append(tel)
            card3.append(sex)
        elif i == 4:
            card1[name1] = name
            print("修改成功!")
        elif i == 6:
            card2[tel1] = tel
            print("修改成功!")
        elif i == 7:
            card3[sex1] = sex
            print("修改成功!")
print("现在所有名片如下:\nname: %s\ntel: %s\nsex: %s" % (card1, card2, card3))


