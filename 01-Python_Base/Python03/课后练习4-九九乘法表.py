#  正序九九乘法
#  一共9行  9列   竖正序增加  行正序增加
#   定义两个变量
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d * %d = %d " % (col, row, row * col), end="\t")
#         col += 1
#     row += 1
#     print()


# 倒序九九乘法
# 行数递减   列数增加
row = 9
while row > 0:
    col = 1
    while col <= row:
        print("%d * %d = %d " % (col, row, row * col), end="\t")
        col += 1
    row -= 1
    print()