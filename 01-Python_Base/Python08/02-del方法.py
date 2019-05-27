class Dog:

    def __init__(self):
        self.type = "小狗"

    def __del__(self):
        print("当对象即将销毁时会调用")
        print("%s 将要销毁" % self.type)


dog1 = Dog()
a = dog1
del dog1  # a和dog1引用相同的内存地址 删除dog1   a在引用内存没有销毁
print("test1")
del a
print("test2")  # 删除a后没有引用对象直接销毁
dog1 = Dog()  # 重新定义
