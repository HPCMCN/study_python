# age = int(input("上报年龄:\n"))
# if age >= 18:
#     print("可以进入网吧嗨皮!")
# else:
#     print("回家写作业吧!")

# number = int(input("请输入数字:\n"))
# if number:
#     print("数字非0")
# else:
#     print("数字为0")
# print("无论是否比较  本行都要打印")


"""
1. 练习1: 定义⼀个整数变量 age ，编写代码判断年龄是否正确
条件语句,要求⼈的年龄在 0-120 之间
2. 练习2: 定义两个整数变量 python_score 、 c_score ，编写代码判断成绩
要求只要有⼀⻔成绩 > 60 分就算合格
3. 练习3: 定义⼀个布尔型变量 is_employee ，编写代码判断是否是本公司员⼯
如果不是提示不允许⼊内
"""
 # 定义一个age    age属于(0,120)
# age = int(input("请输入判断年龄:\n"))
# if age >= 0 and age <= 120:
#     print("年龄正确!")
# else:
#     print("年龄出错!")
#
# python_score = int(input("请输入你Python分数:\n"))
# c_score = int(input("请输入你c语言分数:\n"))
# if python_score > 60 or c_score > 60:
#     print("成绩合格!")
# else:
#     print("再接再厉!")
#
# text = 0
# is_employee = input("判断你的公司:\n")
# if is_employee == "黑马":
#     text = True
#     print(text)
#     print("可以入内")
# else:
#     text = False
#     print(text)
#     print("禁止入内")

# """
# 1. 定义 holiday_name 字符串变量记录节⽇名称
# 2. 如果是 情⼈节 应该 买玫瑰／看电影
# 3. 如果是 平安夜 应该 买苹果／吃⼤餐
# 4. 如果是 ⽣⽇ 应该 买蛋糕
# 5. 其他的⽇⼦每天都是节⽇啊……
# """
# holiday_name = input("请输入节日名称:\n")
# print("%s当然应该:" % holiday_name)
# if holiday_name == "情人节":
#     print("买玫瑰/看电影")
# elif holiday_name == "平安夜":
#     print("买苹果/吃大餐")
# elif holiday_name == "生日":
#     print("买生日蛋糕")
# else:
#     print("吃喝玩啊!")

#
# """
# 1. 定义布尔型变量 has_ticket 表示是否有⻋票
# 2. 定义整型变量 knife_length 表示⼑的⻓度，单位：厘⽶
# 3. ⾸先检查是否有⻋票，如果有，才允许进⾏ 安检
# 4. 安检时，需要检查⼑的⻓度，判断是否超过 20 厘⽶
# 如果超过 20 厘⽶，提示⼑的⻓度，不允许上⻋
# 如果不超过 20 厘⽶，安检通过
# 5. 如果没有⻋票，不允许进⻔
# # """
# knife_length = 0
# has_ticket = input("判断是否持有车票:\n")
# if has_ticket == "有" or has_ticket == "y" or has_ticket == "Y" or has_ticket == "是" or has_ticket == "Yes":
#     print("可以进行安检!")
#     knife_length = float(input("确定刀的长度:\n"))
#     if 0 <= knife_length <= 20:
#         print("通过!")
#     elif knife_length > 20:
#         print("禁止入内!")
#     else:
#         print("输入错误!")
# else:
#     print("小伙子,去买张票再来!")

import random
you = input("请出拳:\n石头/剪刀/布")
computer = random.randint(1,3)
if you == "石头" or you == "1":
    text = 1
elif you == "剪刀" or you == "2":
    text = 2
elif you == "布" or you == "3":
    text = 3
else:
    text = 0
if text == 0:
    print("输入错误!")
else:
    if you == text:
        print("平局!")
    elif (text == 2 and you == 1) or (text == 1 and you == 3) or (text == 3 and you == 2):
        print("挑战成功!")
    else:
        print("挑战失败!")
















