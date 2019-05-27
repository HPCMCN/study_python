class Dog:

    def __init__(self, name):
        self.name = name
        self.type = "狗"


class XTQ(Dog):
    # 如果子类想定义自己独有的属性, 重写init方法, 但重写之后父类的属性就无法继承, 如果还想继承需要用super
    def __init__(self, name):
        # Dog.__init__(self, name)
        super(XTQ, self).__init__(name)
        self.age = 10
        self.type = "大狗"


xiaotq = XTQ("大黑")
print(xiaotq.age)
print(xiaotq.type)

