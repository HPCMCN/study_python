# i = 1
# hei = 0
# while i <= 99997:
#     hei += 1
#     print("媳妇儿,我错了%d" % hei)
#     i += 1

# i = 1
# PP = 0
# while i <= 99:
#     PP += i
#     i += 1
# print("i是%d,PP是%d" % (i, PP))


# i = 0
# while i < 10:
#     if i == 5:
#         print("找到所要获取的密码")
#         break
#     i += 1
#     print(i)
# print("测试%d" % i)

#
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         print("跳过5!")
#         continue
#     print(i)
# print("测试%d" % i)


#
# i = 1
# while i < 6:
#     print("*" * i, end="")
#     i += 1
#
# i = 1
# row = 1
# while i <= 9:
#     i += 1
#     if i <= (row + 1):
#         print("%d * %d = %d\t" % (i, row, i * row), end="")
#         print("")
#         row += 1
#         i = 1
#         if row == 10:
#             break
#         continue


# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d * %d = %d" % (col, row, row * col), end="\t")
#         col += 1
#     print("")
#     row += 1
#


# name_list = ["张三", "李四", "王五"]
# for name in name_list:
#     print(name)
# i = 0
# while i < 3:
#     list_count = name_list[i]
#     print(list_count)
#     i += 1
import random
people = ["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8"]
office1 = []
office2 = []
office3 = []
i = 0
while i < 8:
    text = people[i]
    num = random.randint(0, 2)
    if num == 0:
        office1.append(people[i])
    elif num == 1:
        office2.append(people[i])
    else:
        office3.append(people[i])
    i += 1
print("第一个房间有%d个人:\n" % (len(office1)))
print(office1)
print("\n第二个房间有%d个人:\n" % (len(office2)))
print(office2)
print("\n第三个房间有%d个人:\n" % (len(office3)))
print(office3)