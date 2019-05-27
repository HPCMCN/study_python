import random
teachers = int(input("请输入老师个数:\n"))
office2 = int(input("请输入教室数量:\n"))
teacher = []
office = []
if teachers >= office2:
    num = 0
    while num < teachers:
        teacher.append(num + 1)
        num += 1
    num1 = 0
    while num1 < office2:
        office.append([])
        num1 += 1
    m = 0
    for names in office:
        office_num = random.randint(0, (len(office) - 1))  # 随机生成教室
        teacher_num = random.randint(0, (len(teacher) - m - 1))  # 随机生成老师  数量和教室数量一致
        office[office_num].append(teacher[teacher_num])
        del teacher[teacher_num]  # 挑出来一个老师删除一个并且重新定义len的个数
    for names in teacher:  # 先给每个教室随机一个老师  在让老师随机生成  防止出现空列表
        index = random.randint(0, (len(office) - 1))
        office[index].append(names)
    i = 1
    office.sort()  # 先升序一下
    for office1 in office:
        print("\n第 %d 个房间有 %d 人:\n" % (i, len(office1)))
        for name in office1:
            print("%s  " % name, end="")
        i += 1
else:
    print("\n想啥呢,你给我分个试试!")