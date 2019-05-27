import random
te = ["A", "B", "C", "D", "E", "F", "G", "H"]
of = [[], [], []]
for names in te:
    index = random.randint(0, (len(of) - 1))
    of[index].append(names)
i = 1
for of1 in of:
    print("第 %d 个房间有 %d 人:\n" % (i, len(of1)))
    for name in of1:
        print(name, end="")
    print("\n", "*" * 20)
    i += 1
