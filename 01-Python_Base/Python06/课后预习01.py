# 列表推导式

# a = [x for x in range(101)]
# b = [a[x+1:x+4] for x in range(0, 100, 3)]
# b = [a[3*x+1:3*x+4] for x in range(34)]
# b = [a[x:x+3] for x in range(101) if x % 3 == 1]
# print(b)


def fun(a, b, opt):
    print("a = %d" % a)
    print("b = %d" % b)
    print("result = %d" % opt(a, b))


fun(1, 2, lambda x, y: x + y)

import os

os.remove("666.txt")
os.remove("666.xls")
