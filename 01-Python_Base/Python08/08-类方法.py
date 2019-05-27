"""
私有类属性: 在类属性名字前面加双下划线
"""


class Dog:

    __type = "小狗"  # 类属性

    @classmethod
    def set_type(cls, type1):
        print(cls)
        if type1.count("狗"):
            cls.__type = type1
        else:
            print("数据中不包含狗字")

    @classmethod
    def get_type(cls):
        return cls.__type


dog1 = Dog()
Dog.set_type("大黑")
print(Dog.get_type())

