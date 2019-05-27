# set1 = {1, 2, 3, 6, 4, 5, 6, 1, 6, 5, 4, 5, 6, 3}
# print(set1)
# print(type(set1))

# for _ in range(1, 101):
#     print(_, end="")

# list1 = [(i**2) for i in range(1, 11) if i % 2 == 0]
# print(list1)
#
# list1 = ["666" for _ in range(10)]
# print(list1)

# list1 = ["zhangsan", "lisi", "wangwu"]
# list2 = [name for name in list1 if len(name) > 5]
# print(list2)


"""
请写出⼀段 Python 代码实现分组⼀个 list ⾥⾯的元素,⽐如 [1,2,3,...100]变成[[1,2,3],[4,5,6]....]
"""
#
# a = [name for name in range(101)]
# b = [a[x:(x+3)] for x in a if x % 3 == 1]
# print(b)
