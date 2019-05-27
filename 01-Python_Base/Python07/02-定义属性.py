"""
属性是用来记录对象的属性, 类似于变量
定义属性格式: 对象.属性名 = 值
"""


class Dog:
    """狗类"""
    def drink(self):
        print("喝王老吉")


dog1 = Dog()
dog1.drink()

dog1.name = "旺财"  # 首次给对象属性赋值就是定义属性
dog1.name = "小黑"  # 修改属性记录的值
dog1.age = 2

print(dog1.name)
print(dog1.age)
