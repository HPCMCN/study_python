"""
文件读取
1.如果比较大  read读取可能会出现内存峰值闪退   可以再read(从前往后指定多少字符)  readlines()列表  每一行返回一个元素并且加了一个换行符
2.用while True 来实现
"""


# with open("123.txt", "r") as f:
#     while True:
#         content = f.readline()
#         if len(content) == 0:
#             break
#         print(content, end="")


with open("123.txt", "r") as f:

        content = f.readline()

        print(content, end="")