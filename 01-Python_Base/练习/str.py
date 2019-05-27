print("请输入一串字符串:", end="")
while True:
    str1 = input()
    if str1.isalpha():
        list1 = []
        for i in str1:
            list1.append(i)
        print("第一个字符%s出现%d次" % (list1[0], list1.count(list1[0])))
        break
    else:
        print("请重新输入:", end="")

