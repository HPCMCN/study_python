"""
要修改一个对象的属性有几种方法,分别是什么?
直接方法  和间接方法
私有属性的安全性的一般处理方式是什么?
将属性私有化, 通过类方法进行处理  创建一个get和set进行外部获取和修改
要想将一个属性私有化,该怎么做?
加__
在Python中属性有哪几种权限?
共有属性   和 私有属性
定义一个people类,其中要有类的初始化函数(带参数name).
class People:

    def __init__(self, name):
        self.name = name



如何将上述的name改成私有属性?
class People:

    def __init__(self, name):
        self.__name = name
此时在类外还能访问到name吗?
不能再外部直接访问
在类内可以访问到name吗?
只能在内部进行直接访问
如果想要在类外访问到name该怎么办?
如果想要在类的外部使用name必须要在类内部创建一个方法get进行获取,创建一个set方法进行修改
在类内定义一个可以调用私有属性name的函数.
class People:

    def __init__(self):
        self.__name = "ww"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name = name
如果要想修改私有属性name该怎么办?
通过创建set类方法进行修改   或者在类里面修改
大家是如何理解单继承的?
单继承, 就是一个子类只继承一个父类
请写出单继承的格式?
class Test1:

    @staticmethod:
    def __init__():
        print("test1")


class Test2(test1):

    pass


请写出一个car基类,BMW类继承于car类,基类中有init方法(包含name,color)和run方法.
class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def run(self):
        print("车子跑起来")

class BMW(Car):

    pass


如果子类中没有定义init方法,但是要实例化一个对象,那此时会调用父类的构造方法吗?
会
如果子类重写了init方法,那么在实例化对象的时候,你觉得会调用哪个构造方法,是父类的还是子类的?
子类的
当子类重写init方法,在实例化对象的时候,如果想要调用父类的init方法该怎么办?
手动调用, 在子类init中添加继续调用父类
类中的私有属性能通过对象直接访问吗?
不能
要想访问类中的私有属性该怎么办?
通过类方法间接的访问
基类中的私有属性能被子类继承吗?
不能, 也不能被访问
那么私有属性存在的意义是什么?
防止该属性被随意修改, 保证属性的稳定性,  保证安全
self只想内存地址, class指向类
如何理解多继承?
一个子类拥有多个父类
写出一个简单的多继承案例.
class 子类名(父类1, 父类2, 父类3)
    属性
    方法
如果多个父类中有相同的方法,那么子类在调用的时候,挑用哪个?
先访问子类本身,如果不存在就从前往后访问父类
如何理解重写?
当不想使用父类或者父类不能满足子类要求时重写父类
下面有一个类,请重写类中的方法
class Test1:
# class Car:
#
#     def run(self):
#         print("奔驰在路上!")
#
#
# class Test1(Car):
#
#     def run(self):
#         print("test")
#
#
# test = Test1()
# test.run()
你是如何理解多态的?
一种类型  多种形态
请解读出多态一章中python"鸭子类型"程序的运行结果.

简述你自己对类属性的理解?
类属性就是类对象拥有的属性, 它被所有类对象的实例对象所拥有
请写出一个简单的类,其中包含公有属性,私有属性.
class Test:

    def __init__(self, name)
        self.name = name
        self.__age = 18


请判断下面类中哪些是类属性,哪些是实例属性?
 class Car(obj):
     addr = "china"  # 类属性
     def __init__(self):
         self.name = 'changcheng'   #实例属性
         self.money = 100000  # 实例属性
如果要在类外修改类属性该怎么做?
通过调用类对象进行修改
实例属性修改的方式是什么?
类名.实例属性名() = 修改值
简述你对类方法的理解?
类方法是类对象所拥有的方法, 需要用@classmethod来表示为类方法
对于类方法的参数有什么要求吗?
参数必须对应  第一个必须是类对象   一般作为cls作为第一个参数
类方法可以通过哪几种方式引用?
实例对象, 类对象引用
类方法的用途?
对类属性进性修改
如何使用静态方法?
@staticmethod
def xxxx
如何在静态方法中引用类属性?
必须通过类对象引用
动物:吃,喝,跑,玩
猫:喵喵叫
狗:旺旺叫
猫狗继承于动物,并且有2、3钟自己的属性.
class Animals:

#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, eat):
#         print("吃点%s" % eat)
#
#     def drink(self, drink):
#         print("喝点%s" % drink)
#
#     def run(self):
#         print("跑一跑")
#
#     def play(self):
#         print("玩一玩")
#
#
# class Dog(Animals):
#     ""狗""
#     def call(self):
#         print("汪汪")
#
#
# class Cat(Animals):
#     ""猫""
#     def call(self):
#         print("喵喵")
#
#
# dog1 = Dog("dog1")
# dog1.drink("王老吉")
# dog1.call()
#
# cat1 = Cat("cat1")
# cat1.run()
# cat1.call()
"""
# 定义一个人的基类,类中要有初始化方法,方法中要有人的姓名,年龄.
# 将类中的姓名和年龄私有化.
# 提供获取用户信息的函数.
# 提供获取私有属性的方法.
# 提供可以设置私有属性的函数.
# 设置年龄的范围(0-100).


# class People:
#     """人类"""
#     def __init__(self):
#         self.__name = None
#         self.__age = None
#
#     def set_age_name(self, name, age):
#         if age in range(101):
#             self.__name = name
#             self.__age = age
#         else:
#             print("输入不合法")
#
#     def get_age_name(self):
#         if self.__name:
#             return "%s的年龄为%s" % (self.__name, self.__age)
#
#
# people1 = People()
# people1.set_age_name("ww", 999)
# print(people1.get_age_name())

# 创建一个动物的基类,其中有一个run方法
# 创建一个cat类继承于动物类
# 创建一个dog类继承于动物类
# cat类中不仅有run方法还有eat方法
# dog类中方法同上
# 编写测试程序已验证

#
# class Animals:
#     """动物类"""
#     def __init__(self):
#

# 在类内定义一个可以重新设置私有属性name的函数条件为字符串长度小于10,才可以修改.
# class test1:
#
#     def __init__(self):
#         self.__name = None
#
#     def set_name(self, name):
#         if len(name) < 10:
#             self.__name = name
#         else:
#             print("字符长度超过10位")
#
#     def get_name(self):
#         return "name is %s" % self.__name


# 在创建一个类之后需要调用什么函数?
# __init__
# del()方法是手动调用还是类默认调用?
# 默认
# 如何访问对象的属性?
# str   print(class)
# 创建一个动物类,并通过init方法接受参数(name),并打印init被调用.
#
# 在动物类中定义一个析构方法,使其在删除的时候自动被调用,并打印del被调用.
# class Animals:
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, eat):
#         print("吃点%s" % eat)
#
#     def drink(self, drink):
#         print("喝点%s" % drink)
#
#     def run(self):
#         print("跑一跑")
#
#     def play(self):
#         print("玩一玩")
#
#     def __del__(self):
#         print("当删除的是否来调用")
#
# xx = Animals("八公")
# print(xx)
# xxx = xx
# print(xx)
# print(xxx)
# xxxx = xxx
# del xx
# print(xx)
# print(xxx)
# del xxx
# print(xx)
# print(xxx)
# del xxxx

# 实例化一个dog对象取名"八公"
# 将实例dog赋值给dog1和dog2.
# 分别删除dog,dog1和dog2,并在删除之前分别打印删除对象dog, dog1和dog2.
# 观察运行结果发现什么问题?
# 上述结果说明什么问题?