class Dog:

    def __init__(self):
        self.__age = None  # 私有属性

    def set_age(self, age):
        if 20 >= age >= 0:
            self.__age = age
        else:
            print("输入不合法")
            self.__info("age")

    def get_age(self):
        return self.__age

    def __info(self, name):  # 私有方法
        print("%s 属性赋值不成功" % name)


dog1 = Dog()
dog1.__age = 90  # 仅仅是重新构建了一个变量
dog1.set_age(10)  # 强制修改私有属性和方法就像是在类外面重新构建了一个和类属性或方法同名的变量   没有实质性作用
print(dog1.get_age())
