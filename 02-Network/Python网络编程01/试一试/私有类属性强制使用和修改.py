class Test:

    def __init__(self):
        self.__name = 100


t = Test()
print(dir(t))
t._Test_name = 50

print(t._Test__name)
t1 = Test()
print(t1._Test__name)
