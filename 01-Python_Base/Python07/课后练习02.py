import random
"""
类就好比一个模型，可以预先定义一些统一的属性或者方法，然后通过这个模型创建出具体的对象
对
类是抽象的，而对象是具体的、实实在在的一个事物
对
拥有相同(或者类似)属性和行为的对象都可以抽像出一个类
对
一个类只能创建出一个对象
错
__init__方法在创建对象时，可以完成一些初始化的操作，完成一些默认的设定
对
类是抽象的，而对象是具体的、实实在在的一个事物
对
__str__方法可以没有返回值
错
__str__方法可以返回除字符串以外的其他类型的数据
错

"""

# class Test:
#     def __init__(self):
#         self.a = "abcdef"
#
#     def test1(self, args1):
#         print("test1----", args1)
#         print("test1----", self.a)
#
#     def test2(self):
#         print("test2---", self.a)
#
#     def test3(self, args3=300):  # 缺少冒号
#         print("test3---", args3)
#
#
# t = Test()  # 创建对象
# t.test1("args1")
# # t.test1(args1)
# t.test2()
# # t.test2("abc",666)
# t.test3(900)
# t.test3()

"""
任意定义一个动物类
使用__init__方法，在创建某个动物对象时，为其添加name、age、color,food等属性，如“熊猫”，5,“黑白”，66，“竹子”
为动物类定义一个run方法，调用run方法时打印相关信息，如打印出“熊猫正在奔跑”
为动物类定义一个get_age方法，调用get_age方法时打印相关信息，如打印出“这只熊猫今年5岁了”
为动物类定义一个eat方法，调用eat方法时打印相关信息，如打印出“熊猫正在吃竹子”
通过动物类分别创建出3只不同种类的动物，分别调用它们的方法，让他们“跑起来”，“吃起来”
"""

#
# class animal:
#     """动物类"""
#
#     def __init__(self, name, age, color, food):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.food = food
#
#     def run(self):
#         print("%s快跑" % self.name)
#
#     def get_age(self):
#         print("这只%s今年%s岁了" % (self.name, self.age))
#
#     def eat(self):
#         print("这只%s正在吃%s" % (self.name, self.food))
#
#
# panda1 = animal("熊猫", 5, "花色", "竹子")
# panda1.eat()
# panda1.get_age()
#
# dog = animal("小狗", 6, "黄色", "狗粮")
# dog.run()
# dog.eat()


# class SweetPotato:
#     """烤地瓜"""
#
#     def __init__(self, name, time, condiment):
#         self.name = name
#         self.state = "生的"
#         self.time = time
#         self.condiment = condiment
#
#     def barbecue(self):
#         if 0 <= self.time < 3:
#             self.state = "生的"
#         elif 3 <= self.time < 6:
#             self.state = "快熟了"
#         elif 6 <= self.time < 9:
#             self.state = "熟了"
#         else:
#             self.state = "焦了"
#
#     def __str__(self):
#         return "名字:%s\n状态:%s\n烧烤时间:%s\n添加剂:%s\n" % (self.name, self.state, self.time, self.condiment)
#
#
# sweet_potato1 = SweetPotato("红薯", 0, "防腐剂")
# sweet_potato1.barbecue()
# print(sweet_potato1)
#
# sweet_potato1 = SweetPotato("红薯", 5, "辣椒酱")
# sweet_potato1.barbecue()
# print(sweet_potato1)
#
# sweet_potato1 = SweetPotato("红薯", 10, "胡椒粉")
# sweet_potato1.barbecue()
# print(sweet_potato1)

#
# class SweetPotato:
#     """自动版烤地瓜"""
#
#     def __init__(self, name):
#         self.name = name
#         self.state = "生的"
#         self.time = 0
#         self.condiment = []
#
#     def barbecue(self, time=0.1):
#         while True:
#             self.time += time
#             if 0 <= self.time < 3:
#                 self.state = "生的"
#             elif 3 <= self.time < 6:
#                 self.state = "快熟了"
#             elif 6 <= self.time < 9:
#                 self.state = "熟了"
#                 break
#             else:
#                 self.state = "焦了"
#
#     def auto_condiment1(self):
#         condiment = random.randint(0, 3)
#         print(condiment)
#         self.condiment.append(["番茄酱", "沙拉酱", "芥末酱", "辣椒酱"][condiment])
#
#     def __str__(self):
#         return "名字:%s\n状态:%s\n烧烤时间:%s\n添加剂:%s\n" % (self.name, self.state, self.time, self.condiment)
#
#
# sweet_potato1 = SweetPotato("红薯")
# sweet_potato1.auto_condiment1()
# sweet_potato1.barbecue(0.1)
# print(sweet_potato1)
# #
# sweet_potato1.auto_condiment1()
# sweet_potato1.barbecue(5)
# print(sweet_potato1)
#
# sweet_potato1.barbecue(10)
# sweet_potato1.auto_condiment1()
# print(sweet_potato1)

