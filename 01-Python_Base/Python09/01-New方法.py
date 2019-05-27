# 模拟创建一个实例对象
# 1. 调用魔法方法__new__ 创建并返回一个对象内存空间
# 2. 调用__init__ 给对象赋值
# 3. 返回对象


class Dog:

    def __init__(self):
        self.name = "小黑"


dog1 = Dog()


def Dog_instance():

    dog = object.__new__(Dog)  # 调用基类开辟内存空间
    # dog = Dog.__new__(Dog)  # 调用Dog开辟内存空间,实质还是调用Dog父类object
    dog.__init__()  # 调用Dog的init给对象赋值
    return dog  # 返回对象


dog2 = Dog_instance()
print(dog2)
print(dog1)
print(dog1.name)
print(dog2.name)