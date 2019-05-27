class Dog:

    def __init__(self):
        self.__age = 10

    def __info(self):
        print("xxxx")

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return self.__age

class XTQ(Dog):

    def eat(self):
        pass


xtq = XTQ()
print(xtq.__init__())
xg = Dog()
print(xg.__str__())
