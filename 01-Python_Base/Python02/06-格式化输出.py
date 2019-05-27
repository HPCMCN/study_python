# price = 100.05
# print("苹果的单价为:%.2f元." % price)  # 格式化占位符  f默认保留6位小数

name = "小明"
print("我的名字叫 %s,请多多关照!" % name)

student_num = 1
print("我的学号是%06d" % student_num)

price = 9.00
weight = 5.00
money = price * weight
print("苹果单价 %.2f元,重量是 %.2fkg,总价是 %.2f元." % (price, weight, money))

scale = 0.10
print("数据比例是 %.2f%%" % (scale * 100))
