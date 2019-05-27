# 变量作用: 在编程中方便存取数据

# 把变量放在print中输出
price = float(input("请输入价格:"))
weight = 7.5
total_price = price * weight
you_hui = 1
print("原价:%.2f元" % total_price)
total_price = total_price - you_hui
print("价格:%.2f元" % total_price)
print("优惠:%.2f元" % you_hui)