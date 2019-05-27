"""
思考什么是函数? 为什么要使用函数?
具有独立功能的代码组成的块,在需要的时候调用,让代码更好的高耦合,低内聚
定义、调用函数的格式分别是什么？
def 函数名():
    三引号加函数说明
    函数体
函数名()
编写一段代码，定义一个函数求1-100之间所有整数的和，并调用改函数打印出结果。


def su():
    na = 0
    for name in range(1, 101):
        na += name
    return na


n = su()
print(n)

函数的文档说明有什么用？
增加代码的可读性
给第3题中的函数加一个文档说明。
"""
#
#
# def su():
#     na = 0
#     for name in range(1, 101):
#         na += name
#     return na
#
#
# n = su()
# print(n)


"""
什么是函数的参数？为什么使用参数？
函数内部使用的参数,使参数更加灵活,方便控制
分别说明什么是“形参”和“实参”。
形参在函数括号内,形参是调用函数时给函数赋的值
编写一段代码，定义一个函数求两个数之间所有整数的和，在调用该函数时传入这两个数的具体值。
def su(a, b):
    na = 0
    b += 1
    for name in range(a, b):
        na += name

    return na


re = su(int(input("请输入起始值")), int(input("请输入结束值")))
print(re)


    
什么是返回值？
函数外部利用函数内部的值需要函数在最后返回出来
将第3题中的计算结果作为返回值打印出来。

函数有哪四种类型？
有参数无返回值   无参数无返回值   有参数有返回值   无参数有返回值
什么是函数的嵌套，写一个简单的函数嵌套：调用test1，在打印函数test1的内容前打印函数test2的内容。
def test1():
    print("test1")


def test2():
    print("test2")
    test()
    print("test2")
    
test2()


定义一个拥有参数的函数并调用，要求把参数打印出来


定义一个拥有返回值的参数并调用，要求调用后，把返回值打印出来
"""


# def su(a, b):
#     na = 0
#     b += 1
#     for name in range(a, b):
#         na += name
#
#     return na
#
#
# re = su(int(input("请输入起始值")), int(input("请输入结束值")))
# print(re)
#


"""
用函数实现一个判断用户输入的年份是否是闰年的程序。
提示：
1.能被400整除的年份 
2.能被4整除，但是不能被100整除的年份
以上2种方法满足一种即为闰年
"""


# def year():
#     """判断是否闰年"""
#     while True:
#         print("退出输入0")
#         num = input("请输入所要的测试年份:\n")
#         if num == "0":
#             break
#         if len(num) == 4 and num.isdecimal():
#             num = int(num)
#             print("格式正确,正在测试...")
#             if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#                 print("%d是闰年" % num)
#             else:
#                 print("%d非闰年" % num)
#         else:
#             print("格式错误,请重新输入!")
#
#
# year()


"""
使用函数求前20个斐波那契数列。
提示：
斐波那契数列：1,1,2,3,5,8,13,21...即: 起始两项均为1，此后的项分别为前两项之和。
"""

#
# def s():
#     """斐波那契数列"""
#     a = 1
#     for i in range(19):
#         a += a
#         print(a)
#         print(i)
#     return a
#
#
# su = s()

