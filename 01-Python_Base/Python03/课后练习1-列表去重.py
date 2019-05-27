# list1 = ["1", "3", "4", "1", "3", "5", "2", "1"]
# list2 = []
# i = 0
# while i < len(list1):
#     name = list1[i]
#     if name not in list2:
#         list2.append(name)
#     i += 1
# list1.clear()
# list1.extend(list2)
# print(list1)


# 把列表中每个元素都取出来   赋给list2   如果重复就删掉
# list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# i = 0
# while i < len(list1):
#     count = list1.count(list1[i])
#     if count == 2:
#         del list1[i]
#         print(list1)
#     i += 1
# print(list1)

#
# list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# i = len(list1)
# while i >= 0:
#     name = list1.pop(0)
#     if name not in list1:
#         list1.append(name)
#     i -= 1
# print(list1)


# list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# i = 0
# while i < len(list1):
#     x = list1.index(list1[i])
#     if i > x:
#         del list1[i]
#         continue
#     i += 1
# print(list1)
name = input("")
list1 = []
for i in name:
    list1.append(i)
print(list1)
a = 0
for m in range(0, (len(list1))):
    count = list1.count(list1[m-a])
    index = list1.index(list1[m-a])
    if count > 1 or list1[index] == " ":
        a += 1
        del list1[index]
print(list1)
