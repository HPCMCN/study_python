list1 = [10, 20, 30, 40, 50]
a = 0
for element in range(len(list1)):
    if list1[element - a] in [30, 40]:
        list1.remove(list1[element - a])
        a += 1
print(list1)
