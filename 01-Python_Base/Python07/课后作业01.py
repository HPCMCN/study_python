"""
如何理解面向对象编程(OOP)
将具有相互关系的数据和操作封装
什么是类，什么是对象
对象包括属性和操作方法
类表示多个对象的共同属性和操作方法的汇聚
"""

"""
python中如何定义一个类
class 名字(大驼峰命名):
    
    def 名字():
    ....

类(class)由哪三个部分构成
定义, 数据, 方法
类名的命名规则是什么
大驼峰命名
python中如何通过类创建对象，请用代码进行说明
class Type1:

    def su_xing(self, xx):
        self.xx = xx
    def__str__(self):
        return xx

xx = class()
xx=xx.su_xing(xx)  # 创建对象
如何在类中定义一个方法，请用代码进行说明
class Type1:
    def __init__(self, ss):
        self.ss = ss
    def su_xing(self, xx):
        self.xx = xx
    def__str__(self):
        return xx

xx = class(ss) # 创建对象
xx=xx.su_xing(xx)  # 调用方法
定义一个People类，使用People类，创建一个mayun对象后，添加company属性，值是"阿里巴巴"；创建一个wangjianlin对象，添加company属性，值是"万达集团"
定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加上颜色属性
定义一个汽车类，并在类中定义一个move方法，然后分别创建BMW_X9、AUDI_A9对象，并添加颜色、马力、型号等属性，然后分别打印出属性值、调用move方法
"""


# class People:
#     """人类"""
#
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
#
#     def __str__(self):
#         return "%s公司  %s" % (self.name, self.company)
#
#
# mayun = People("马云", "阿里巴巴")
# print(mayun)
# wangjianlin = People("王健林", "万达集团")
# print(wangjianlin)

#
# class fruit:
#     """水果类"""
#
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def __str__(self):
#         return "%s 颜色是: %s" % (self.name, self.color)
#
#
# apple = fruit("苹果", "红色")
# orange = fruit("橘子", "黄色")
# watermelon = fruit("西瓜", "绿色")
# print(apple)
# print(orange)
# print(watermelon)


# class car:
#     """水果类"""
#
#     def __init__(self, type1, color, soup):
#             self.type = type1
#             self.color = color
#             self.soup = soup
#
#     def move(self):
#         print("不知道用来干啥")
#
#     def __str__(self):
#         return "型号:%s\n颜色:%s\n马力:%s" % (self.type, self.color, self.soup)
#
#
# BMW_X9 = car("BMW_X9", "白色", "2.0")
#
# print(BMW_X9)
# BMW_X9.move()
# print()
# AUDI_A9 = car("AUDI_A9", "白色", "2.0")
#
# print(AUDI_A9)
# AUDI_A9.move()


"""
__init__方法有什么作用，如何定义
def __init__(self)
__str__方法有什么作用，使用时应注意什么问题
返回的值是str   必须转换成字符串
方法中的"self"代表什么
作为参数传递数据
在类中定义__init__和__str__方法时，必须提供形参吗，第一个形参又必须是self吗？为什么？
必须提供形参  第一个形参必须是self   Python的类的方法的这个特别的参数指代的是对象本身，而按照Python的惯例，它用self来表示
"""

