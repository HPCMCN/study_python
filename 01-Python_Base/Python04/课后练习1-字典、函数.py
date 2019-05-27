"""
有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，
要求每个盒子至少有一个白球，请用程序实现
1 先把三个
"""

# ball = ["a", "b", "c","A", "B", "C",1, 2, 3, 4]
# box = [[],[],[]]
# import random
# m = 0
# for name in ball:
#     while True:
#         i = random.randint(0, 2)
#         if m == (len(ball)-1):  # 如果要求每个盒子大于n个, 直接让if len(box[i]) >= n,在前面加一个条件判断,让变量大于等于填满要求的数量
#             # else 也做相同的添加, 并且保证每个端口变量都在增加.
#             box[i].append(name)
#             m += 1
#             break
#         elif 1 in box[i]:
#             continue
#         elif 2 in box[i]:
#             continue
#         elif 3 in box[i]:
#             continue
#         else:
#             box[i].append(name)
#             m += 1
#             break
# print(box)
#

"""
设计一个程序，实现str.split()方法的替换：
首先输入一个任意长度的字符串
其次输入一个字符，用以分割该字符串，并且分割后的字符串保存到一个列表中
不允许使用str.split()方法
最后打印出该字符串被分割成多少部分、以及这个列表
去掉分割出来的空字符串
如"1234r5678r90r"用r分割，则为["1234","5678","90"] 
"""
# # 输入字符串
# x = input("请输入你要拆分的字符串:")
# # 输入分隔符
# cut = input("请输入分割符:")
# # 遍历整个字符串  判断是否存在该字符   如果存在进行分割    不存在直接报错
# # 首先创建一个列表来保存遍历后的字符
# list1 = []
# m = ""
# n = -1
# for name in x:
#     if name == " ":   # 添加筛选空格
#         continue
#     elif name == cut:
#         list1.append(m)
#         m = ""              # 先添加后删除
#         n += 1
#         if list1[n] == "":
#             del list1[n]
#             n -= 1
#         continue
#     else:
#         m += name
# if m != "":  # 判断在程序退出后m中是否有没有添加到列表的字符串   重新添加到里面
#     list1.append(m)
# # if cut not in x:  # 判断切断是否存在字符串中
# #     print("你输入的字符不存在字符串中,请重试!")
#
# print("该字符串被%s切割成%d部分:\n%s" % (cut, len(list1), list1))
