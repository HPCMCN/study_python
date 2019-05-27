"""
分别定义一个字符串类型的全局变量、列表类型的全局变量。定义函数test1，在函数中分别使用，总结有什么区别？
"""
# str1 = "用于测试"
# list1 = ["测试1", "测试2"]
#
#
# def test1(str1, list2):
#     """"测试专用"""
#
#     str1 = "测试专用"
#     list1[0] = "测试3"
#
#
# test1(str1, list1)
# print(str1, list1)
"""
不可变类型字符串在函数内部修改后不能作用全局  可变类型列表在函数内部修改列表内值全局会发生改变
分别定义一个字符串类型的全局变量、列表类型的全局变量。定义函数test2，在函数中分别修改，总结有什么区别？
分别定义一个字符串类型的全局变量、列表类型的全局变量。定义函数test3，分别将全局变量作为参数传递给test3，并在test3中进行修改，总结有什么区别？
如何理解引用传参，实际传递的是什么？
传参就是把全局变量传递到函数内部使用, 实际上传递的是内存地址
"""

#
# def max_min(*args):
#     """获取最大最小值"""
#     b = args[0]
#     c = args[0]
#     for x in args:
#         if x > b:
#             b = x
#         elif x < c:
#             c = x
#         else:
#             pass
#     return b, c
#
#
# b, c = max_min(5, 1, 0)
# print("最小值是%s, 最大值是%s" % (c, b))


# def factorial(n):
#     """阶乘"""
#     if n > 1:
#         n *= factorial(n-1)
#     elif n == 1:
#         return n
#     return n
#
#
# print(factorial(5))


# def ji_ou(n, a=1):
#     """n以内的奇数和偶数"""
#     list1 = []
#     list2 = []
#     for i in range(n + 1):
#         if i % 2 == 1:
#             list1.append(i)
#         else:
#             list2.append(i)
#     if a == 1:
#         return list1
#     else:
#         return list2
#
#
# print(ji_ou(5))


# def su_su(n):
#     """素数"""
#     list1 = []
#     for i in range(n):
#         if i % 2 == 0 and i > 2:
#             continue
#         elif i in [0, 1]:
#             continue
#         elif i % 3 == 0 and i > 3:
#             continue
#         elif i % 5 == 0 and i > 5:
#             continue
#         elif i % 7 == 0 and i > 7:
#             continue
#         else:
#             list1.append(i)
#     return list1
#
#
# print(su_su(88))

#
# def del1(s, a1, a2):
#     """删除指定的字符串"""
#     s = s[:a1] + s[a1:(a1+a2-1)] + s[(a1+a2):]
#     return s
#
#
# print(del1("sfsfafasfsaf", 5, 5))

# 画三角形和正方形
# def tril(n):
#     """三角形"""
#     for i in range(n):
#         if i == 0:
#             print("*")
#         elif i != (n-1):
#             print("*", " " * i*2, "*", sep="")
#         else:
#             print("* " * n)
#
#
# def square(n):
#     """正方形"""
#     for i in range(n):
#         if i == 0:
#             print("*", " *" * (n-1))
#         elif i != (n - 1):
#             print("*", "  " * (n-1), "*", sep="")
#         else:
#             print("*", " *" * (n - 1))
#
#
# num = input("请输入你要打印的图案:\n1.三角形\n2.正方形")
# n = int(input("请输入边长:"))
# if num == "1":
#     tril(n)
# elif num == "2":
#     square(n)
# else:
#     print("无法识别,请重试")


"""
什么是递归函数？递归函数有什么成立条件？
函数自己调用自己   必须设置一个跳出条件   防止进入死循环
使用递归函数求n的阶乘
"""


# def dg(n):
#     sum1 = n
#     if n > 1:
#         sum1 *= dg(n - 1)
#     else:
#         sum1 = n
#         print("不合法, 你输入的数值为:", end="")
#     return sum
#
#
# print(dg(-11))


"""
定义函数findall，实现对字符串find方法的进一步封装，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，需要找出里面所有的"hello"的位置，最后将返回一个元组(0,10,21,29)，即将h的下标全部返回出来，而find方法只能返回第一个
使用递归的方法打印出前n个斐波那契数列
编写一个函数验证哥德巴赫的猜想：任何一个充分大的偶数（大于等于6）总可以表示成两个素数之和-----要求：将6-100之间的偶数，都用两个素数之和去表示
"""


def findall(str1, name):
    """findall的功能"""
    list1 = []
    s = len(str1)
    str1 = str1.replace(name, "0")
    while True:
        index = str1.find("0")
        if str1[index] == "0":
            str1 = str1[index + 1:]
            s1 = len(str1) - str1.count("0") + (str1.count("0") + 1) * len(name)
            list1.append(s - s1)
        else:
            break
    return type(list1)


list2 = findall("helloworldhellopythonhelloc++hellojava", "hello")
print(list2)


# def fei_bo(m, n=1):
#     """斐波那契数列"""
#     list1 = [1]
#     if n > m:
#         return n, list1
#     else:
#         print(n)
#         n += n
#         list1.append(n)
#         n = fei_bo(m, n)
#
#
#     return n, list1
#
#
# print(fei_bo(10))
