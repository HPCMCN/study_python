# class Num:
#
#     def __init__(self):
#         self.__num = 500
#
#     def set_num(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#     num = property(get_num, set_num)
#
#
# n = Num()
# n.num = 5
# print(n.num)


# class Num:
#
#     def __init__(self):
#         self.__num = 500
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#
# n = Num()
# n.num = 5
# print(n.num)
x = reversed([6, 3, 7, 9, 2])
print(dir(x))
print(x.__reduce__())