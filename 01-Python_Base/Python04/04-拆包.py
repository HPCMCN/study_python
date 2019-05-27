# tuple1 = (2, 3)
# list1 = [10, 30]
# dict1 = {"a": 50, "b": 90}
# # a, b = tuple1
# a, b = dict1
# print(a, b)

#
# a = [1, 2]
# b = a
# print(id(a))
# print(id(b))
# b.append(3)
# print(a)
#
# a = [1, 2]
# b = [1, 2]
# print(id(a))
# print(id(b))
# b.append(3)
# print(a)
#
# import Python04.python_module
# Python04.python_module.test()
# n = Python04.python_module.count
# print(n)

def test(list={}):
    print(list)
    list["name"] = "ww"
    print(list)


test()
test()