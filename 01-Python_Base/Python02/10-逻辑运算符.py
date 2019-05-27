age = int(input("请输入年龄:"))

if 0 <= age <= 120:
    print("是一个正常人")
else:
    print("外星人")


python_score = 120
c_score = 20
if python_score >= 60 or c_score >= 60:
    print("合格")
else:
    print("不合格")


is_employee = True
if not is_employee:
    print("出去")
else:
    print("可以进来玩")
