
class Dog:

    def eat(self):
        print("吃东西")


def test():

    print("test")


count = 2

"""以下是测试代码"""
print(__name__)  # 如果输出是main是程序主动执行, 如果是文件名  表示导入后被动执行
if __name__ == '__main__':
    test()
