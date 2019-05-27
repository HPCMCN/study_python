"""
什么是局部变量？
作用于函数内部, 不用时就会被释放
什么是全局变量？
作用于整个py文件  使用方便   程序结束时释放
局部变量和全局变量有什么区别？（提示：两者的定义、引用、修改）
同上  在函数内部修改全局变量需要生命globle
如果全局变量和局部变量同名会发生什么效果？
不冲突   在函数外用全局变量  在函数中执行到定义后用局部变量
python中可变类型数据有哪些？不可变类型数据有哪些？
可变类型有列表,字典   不可变类型  字符串 整型 元组
函数中return的作用
返回函数中的数据
函数中如果有多个return，会是什么效果
只要执行到一个return就会直接跳出函数不会再执行其他的代码
python中函数的参数类型有哪些
形参和实参 位参  默认参数 *args  关键字参数
什么是缺省参数
默认参数
什么是不定长参数
*args **args
定义一个使用不定长参数的函数，并在函数中打印出参数及其类型，统计传入参数的个数，


def txst(*agrs):
    print(type(agrs))
    print(agrs)

txst(1, 2, 3, 4, 5)


定义一个函数max，接受的参数类型是数值，最终返回两个数中的最大值


def max(a ,b):
    if type(a) and type(b) in [float, int]:
        if a>b:
            return(a)
        elif a<b:
            return(b)
        else:
            return(a, b)
    else:
        print("请输入数值")


a = input("请输入")
b = input("请输入")
max(a, b)

定义一个函数min，接受的参数类型是数值，最终返回两个数中的最小值
同上if a>b和a<b 互换
分别定义加减乘除四个函数实现两个数之间的加减乘除操作

"""

#
# def add(sum2, sum3):
#     """加法"""
#     return sum3 + sum2
#
#
# def sub(sum2, sum3):
#     """减法"""
#     return sum3 - sum2
#
#
# def mul(sum2, sum3):
#     """乘法"""
#     return sum3 * sum2
#
#
# def di(sum2, sum3):
#     """除法"""
#     if sum2 == 0:
#         print(sum2, "不能作为除数")
#         return 0
#     else:
#         return sum3 / sum2
#
#
# def symbol(sum1, sum2, sum3):
#     """检测运算符"""
#     if sum1 == "+":
#         sum3 = add(sum2, sum3)
#     elif sum1 == "-":
#         sum3 = sub(sum2, sum3)
#     elif sum1 == "*":
#         sum3 = mul(sum2, sum3)
#     elif sum1 == "/":
#         sum3 = di(sum2, sum3)
#     else:
#         sum3 = "过于复杂, 无法计算,请输入四则运算符"
#     return sum3
#
#
# sum3 = 0
# sum2 = 0
# sum4 = 0
# i = 0
# m = 0
# while True:
#     sum1 = input("请输入:")
#     if sum1.isdecimal():
#         if i == 0:
#             i += 1
#             sum3 = float(sum1)
#         else:
#             i += 1
#             sum1 = float(sum1)
#     elif sum1 == "":
#         break
#     elif sum1 in ["+", "-", "*", "/"]:
#         sum4 = sum1
#         continue
#     if i != 1:
#         sum3 = symbol(sum4, sum1, sum3)
#         print(sum3)
#     elif sum1.isdecimal() == 0 and sum1 not in ["+", "-", "*", "/"]:
#         print("输入不合法, 请输入数字!")


