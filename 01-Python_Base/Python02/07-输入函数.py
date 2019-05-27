# Python3中input只能接收到字符串类型的数据
# Python2中input接收到的数据可以自动进行推到,如果是字符串必须要手动加双引号
# Python2中row_input和Python3中的input是一样的   但是Python3中没有row_input已经没有了

test = input("请输入想输入的东西:\n")
print(test)
print(type(test))