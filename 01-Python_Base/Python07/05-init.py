"""
__xx__():  魔法方法   运算符重载方法  这些方法会自动调用
"""

class Dog:

    def __init__(self):
        self.type = "狗"
        self.name = "小黑"

    def eat(self,name):
        print("吃东西")
        

dog1 = Dog()
print(dog1.type)
dog1.eat("小黑")
