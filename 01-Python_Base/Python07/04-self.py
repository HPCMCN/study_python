class Dog:

    def eat(self):  # 在方法中想要访问或操作对象的属性时, 尽量用self
        print("%s 吃肉" % self.name)


dog1 = Dog()
dog1.name = "旺财"

dog2 = Dog()
dog2.name = "来福"

dog1.eat()  # 对象调用方法时, 会把调用此方法的对象会作为第一个实参传递给self
dog2.eat()
