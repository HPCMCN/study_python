"""
通过类名创建出来的对象   实例对象
类对象
"""


class Dog:

    def eat(self):
        print(self)
        print("吃狗粮")


class XTQ(Dog):

    def eat(self):
        Dog.eat(self)
        super(XTQ, self).eat()

        print("吃蟠桃")


xtq = XTQ()
xtq.eat()