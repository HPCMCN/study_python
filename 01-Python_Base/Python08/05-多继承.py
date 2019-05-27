class Dog:

    def eat(self):
        print("吃肉肉")


class God:

    def fly(self):
        print("飞一会~")

    def eat(self):
        print("吃仙丹")


"""
如果多继承时, 多个父类, 有同名的方法, 想要调用指定父类的方法?
重写父类方法, 然后手动调用指定父类的方法
"""


class XTQ(God, Dog):

    def eat(self):
        # Dog.eat(self)  # 多继承时, 想要调用指定父类的方法, 类对象去调用
        super(God, self).eat()


xiaotq = XTQ()
xiaotq.eat()
xiaotq.fly()


print(XTQ.__mro__)
