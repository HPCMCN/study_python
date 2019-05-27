"""
类属性: 通过此类创建出来的所有对象共同使用类型
定义在类里面, 方法的外部, 和定义变量一样
"""


class Dog:

    type = "小狗"  # 类属性

    def __init__(self):
        # self.type = "小狗"  # 实例属性
        pass


dog1 = Dog()

dog2 = Dog()

Dog.type = "大狗"
dog1.type = "大大"  # 类属性不能用实例对象去修改, 如果强制修改实际上是给实例对象定义了一个新的实例属性

print(dog1.type)  # 重新生成的新参数
print(dog2.type)
print(Dog.type)

