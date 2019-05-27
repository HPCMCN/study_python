# def func_sum(*args, is_print=False):  # 默认参数放在可变参数后面
#     result = 0
#     print(args)
#     for a in args:
#         result += a
#     if is_print:
#         print(result)
#
#
# func_sum(1, 2, 3, 4, is_print=True)
#
#
# def func1(a, **kwargs):  # **kwarge用来接受多余的关键字参数, 并生成字典
#     print(a)
#     print(kwargs)
#
#
# func1(a=1, b=2, c=3)


def test(a, b):
    print(a)
    print(b)


# list1 = [2, 5]
# test(*list1)
# tuple1 = (5,9)
# test(*tuple1)
# dic1 = {
#     "a": 26,
#     "b": 56
# }
# test(*dic1)
# test(**dic1)