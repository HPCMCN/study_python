"""
列表和普通变量有什么区别
列表可以储存多个元素  变量只能储存一个
怎样测量列表中元素的个数
len(列表)
怎样获取列表的某个元素
列表[位置]
解释什么是越界
获取超出列表中中个数的索引
如何向列表中添加（增）新元素
列表.eppend(元素)
如何删除（删）列表中的某个元素
list.pop(索引)
如何修改（改）列表中的某个元素
list[索引] = "元素"
如何查找（查）列表中的某个元素
index = list.index("元素")
已有列表nums=[11,22,33,44,55],使用for循环遍历列表
已有列表nums=[11,22,33,44,55],使用while循环遍历列表
已有列表nums=[14,22,63,21,5],将其从小到大排序
列表嵌套的格式
使用列表嵌套，完成8名老师随机分配3个办公室
"""

# 已有列表nums=[11,22,33,44,55],使用for循环遍历列表
# 已有列表nums=[11,22,33,44,55],使用while循环遍历列表
# 已有列表nums=[14,22,63,21,5],将其从小到大排序
# 列表嵌套的格式
# 使用列表嵌套，完成8名老师随机分配3个办公室
# import random
# teacher = ["a", "b", "c", "d", "e", "f", "g","h"]
# office = [[], [], []]
# for names in teacher:
#     i = random.randint(0, 2)
#     office[i].append(names)
# i = 0
# for name in office:
#     print("\n第 %d 个房间有 %d 人:\n" % ((i + 1), len(office[i])))
#     office1 = name
#     # print(office[i])
#     for name in office1:
#         print(name, end="")
#     # if i == len(office):
#     #     break
#     i += 1
# # print(office)
# # nums = [14,22,63,21,5]
# nums.sort()
# print(nums)
# nums = [11, 22, 33, 44, 55]

# i = 0
# while i <= (len(nums) - 1):
#     name = nums[i]
#     print(name)
#     i += 1


# for name in nums:
#     print(name)
# name = []
# name.extend(nums)
#
# print(name)
# print(nums)
# nums[1] = 99
# print(name)
# print(nums)

# list1 = []
# while True:
#     name = input("请输入名字(如果输入完成请输入111111):\n")
#     if name == "111111":
#         break
#     list1.append(name)
# for name in list1:
#     print("%s名字第二个字母是: %s" % ((name), (name[1])))

# list1 = []
# while True:
#     name = input("请输入名字(如果输入完成请输入111111):\n")
#     if name == "111111":
#         break
#     list1.append(name)
# import random
# name = random.randint(0, (len(list1)-1))
# print(list1[name], "去扫地")

# 让老师*个数   教室*个数  然后以字符串的形式拆分出来放在重新定义的列表中

# 相当于生成n个随机数 并且随机数总和为m
# 直接让人数在办公室随机生成
# 人数m  一个循环控制办公室n个随机生成
# 第一个要求上限不高于m-n+1


"""本程序有问题暂时用输入式老师找教室.py"""


import random
teachers = int(input("请输入老师个数:\n"))
office2 = int(input("请输入教室数量:\n"))
teacher = []
num = 0
while num < teachers:
    teacher[num].append(num+1)
    num += 1
office = []
num1 = 0
while num1 < office2:
    office[num1].append(num+1)
for names in teacher:
    index = random.randint(0, (len(office) - 1))
    office[index].append(names)
i = 1
for office1 in office:
    print("第 %d 个房间有 %d 人:\n" % (i, len(office1)))
    for name in office1:
        print(name, end="")
    print("\n", "*" * 20)
    i += 1

