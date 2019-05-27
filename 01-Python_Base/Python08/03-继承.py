# 如果两个类中有同名的方法或属性时, 比例B类去继承A类, B类就可以拥有A类中的所有属性和方法
# 父类和 字类
# 所有类都会继承 object 基类
# class Dog:  #经典类写法,  默认继承object


class Dog(object):  # 新式类写法

    def eat(self, food):
        print("吃 %s" % food)


class XTQ(Dog):  # 格式: 类名(父类名)

    pass


xtq = XTQ()
xtq.eat("狗粮")

