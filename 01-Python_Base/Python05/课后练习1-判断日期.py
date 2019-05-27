"""
判断有效日期
用户可以输入"20170327"等三种格式的日期
判断是否是有效日期，如"20170229"不是有效日期，"20171345"不是有效日期
"""


def years_n(years_1):
    """判断是否是闰年"""
    if (years_1 % 4 == 0 and years_1 % 100 != 0) or years_1 % 400 == 0:  # 如果是闰年,判断月份是否符合条件
        print("%04d年为闰年" % years_1)
        a = 1
    else:
        print("%04d年非闰年" % years_1)
        a = -1
    return a


def years_y(years_y1, a):
    p = 0
    if years_y1 in [1, 3, 5, 7, 8, 10, 12]:
        print("%02d月为31天" % years_y1)
        p = 31
    elif years_y1 == 2:
        if a == -1:
            print("%02d月为28天" % years_y1)
            p = 28
        else:
            print("%02d月为29天" % years_y1)
            p = 29
    elif years_y1 in [4, 6, 9, 11]:
        print("%02d月为30天" % years_y1)
        p = 30
    else:
        print("格式错误")
    return p


def years_r(years_r1, a, p):
    """判断日期"""
    if years_r1 in range(1,31):
        if years_r1 <= p:
            print("日期格式正确!")
        else:
            print("格式错误")
    else:
        print("格式错误")

while True:
    years = input("请输入要判定的时间:\n")
    print("如需退出请按0")
# 切片切去年  月  日
    for name in years:
        if name not in "0123456789":
            print("格式有误!")
            break
    else:
        if years == "0":
            break
        elif len(years) == 8:
            years_n1 = int(years[:4])
            years_y1 = int(years[-4:-2])
            years_r1 = int(years[-2:])
            p = years_n(years_n1)
            q = years_y(years_y1,p)
            if q != 0:
                years_r(years_r1, p, q)
        else:
            print("格式有误")
print("退出系统!")


# 判断年是否时闰年


# 判断是否时12个月
# 判断日期是否在31天内