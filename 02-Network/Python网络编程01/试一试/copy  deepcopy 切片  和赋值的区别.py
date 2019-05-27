import copy
a = [1, 2, 3]
b = [4, [56, 32], 6]
c = [a, b]
d = c
e = copy.copy(c)
f = copy.deepcopy(c)
h = c[:]
print("c 原变量 "+str(id(c)), c)   # 原变量
print("d 赋值 "+str(id(d)), d)   # 赋值
print("e copy "+str(id(e)), e)   # copy
print("f deepcopy "+str(id(f)), f)   # deepcopy
print("h 切片 "+str(id(h)), h)   # 切片
c.append(1)
print("*"*20)
print("c 原变量 "+str(id(c)), c)   # 原变量
print("d 赋值 "+str(id(d)), d)   # 赋值
print("e copy "+str(id(e)), e)   # copy
print("f deepcopy "+str(id(f)), f)   # deepcopy
print("h 切片 "+str(id(h)), h)   # 切片
a.append(9)
print("*"*20)
print("c 原变量 "+str(id(c)), c)   # 原变量
print("d 赋值 "+str(id(d)), d)   # 赋值
print("e copy "+str(id(e)), e)   # copy
print("f deepcopy "+str(id(f)), f)   # deepcopy
print("h 切片 "+str(id(h)), h)   # 切片
b[1].append(2222)
print("*"*20)
print("c 原变量 "+str(id(c)), c)   # 原变量
print("d 赋值 "+str(id(d)), d)   # 赋值
print("e copy "+str(id(e)), e)   # copy
print("f deepcopy "+str(id(f)), f)   # deepcopy
print("h 切片 "+str(id(h)), h)   # 切片
