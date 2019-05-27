import random
list5 = ["1", "2", "3", "4", "5", "6", "7", "8"]
list1 = []
list2 = []
list3 = []
ls1 = 0
ls2 = 0
ls3 = 0
i = 0
while i < len(list5):
    a = random.randint(1, 3)
    name = list5[i]
    if a == 1:
        list1.append(name)
        ls1 = len(list1)
    elif a == 2:
        list2.append(name)
        ls2 = len(list2)
    else:
        list3.append(name)
        ls3 = len(list3)
    i += 1
print("第一个房间有%s人,分别是:" % ls1, end="\n\n")
print(list1, "\n")
print("第二个房间有%s人,分别是:" % ls2, end="\n\n")
print(list2, "\n")
print("第三个房间有%s人,分别是:" % ls3, end="\n\n")
print(list3, "\n")



