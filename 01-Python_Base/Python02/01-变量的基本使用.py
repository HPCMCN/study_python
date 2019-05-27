# # 定义变量   格式:  变量 = 值
# # 变量中实际存的是内存地址,   目的是为了提升性能,减少不必要的操作
# # 首次创建变量
# qq_num = 10000
# qq_pwd = 11111
# print(qq_num)
# print(qq_pwd)


# # 变量作用: 在编程中方便存取数据
#
# # 把变量放在print中输出
# price = float(input("请输入价格:"))
# weight = 7.5
# total_price = price * weight
# you_hui = 1
# print("原价:%.2f元" % total_price)
# total_price = total_price - you_hui
# print("价格:%.2f元" % total_price)
# print("优惠:%.2f元" % you_hui)



# print("开始")
# name = "小明"  # string  字符串
# print(type(name))
# name = 30
# print(type(name))
# age = 18  # integer  整型
# print(type(age))
# boy = True  # bool  布尔类型   T 真   F 假
# print(type(True))
# height = 1.75  # float  浮点类型
# print(type(height))
# weight = 75.0
# print("完成")
#
last_name = "张"
first_name = "三"
name = last_name + first_name
name = name * 8
print(name)

