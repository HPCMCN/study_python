# def fibo(n, num=1):
#     """斐波那契上限"""
#     num += num
#     if n > num:
#         list1.append(num)
#         fibo(n, num)
#     elif num < 1:
#         list1.append(num)
#
#
# n = int(input("请输入上限:\n"))
# if n >= 0:
#     list1 = [1, 1]
#     fibo(n)
#     print(list1)
# else:
#     print("输入不合法")


# list1 = []
#
#
# def feibonaqi(n, num1=1, num2=1):
#     """斐波那契数列个数"""
#     if n <= 0:
#         return
#     elif n == 1:
#         list1.append(num1)
#     elif len(list1) < n:
#         list1.append(num1)
#         list1.append(num2)
#
#         num1 = num2 + num1
#         num2 = num2 + num1
#         feibonaqi(n, num1, num2)
#     else:
#         return
#
#
# nu = int(input("请输入要的数量:\n"))
# feibonaqi(nu)
# print(list1)


# def recur_fibo(n):
#
#     if n <= 1:
#         return n
#     else:
#         return recur_fibo(n - 1) + recur_fibo(n - 2)
#
#
# nterms1 = int(input("22222"))
# if nterms1 <= 0:
#     print("1111")
# else:
#     print("斐波那契数列:")
#     for i in range(nterms1):
#         print(recur_fibo(i))

#
# n = 100
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, "是素数")
#
# print("%")


# str1 = "abcdefgh"
# str1 = str1.center(19)
# print(str1)

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 6, 7, 8]
# n = max(list2)
# print(n)

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if n >= 3:
#         return fibo(n-1)+fibo(n-2)
#
#
# i = 1
# while i <= 50:
#     print(fibo(i))
#     i += 1
