import random
te = [1, 2, 3, 4, 5, 6, 7, 8]
te1 = []
te2 = []
te3 = []
i = 0
while i < len(te):
    of = random.randint(1, 3)
    m = int(te[i])
    if of == 1:
        te1.append(m)
    elif of == 2:
        te2.append(m)
    else:
        te3.append(m)
    i += 1
print("第一个教室有%d人:\n" % (len(te1)),te1)
print("第二个教室有%d人:\n" % (len(te2)),te2)
print("第三个教室有%d人:\n" % (len(te3)),te3)
