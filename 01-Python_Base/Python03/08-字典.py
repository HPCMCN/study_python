import sys
dict1 = {
    "name": "张三",
    "age": "18",
    "boy": "True"
}

name = dict1["name"]  # 必须加引号  用中括号
print(name)

dict1["shen"] = 411  # 添加指定键
print(dict1)

dict1["shen"] = 524  # 添加指定键,  如果存在会覆盖
print(dict1)

del dict1["name"]  # 删除指定键
print(dict1)


# dict1.pop("age")  # 必须指定键值   字典没有顺序可言
# print(dict1)
#
# test = dict1.pop("age")  # 删除并返回给test
#
# dict1.clear()  # 清空字典
# print(dict1)
#
#
# dict1.setdefault("age1", 20)  # 如果存在什么都不做   如果不存在  添加到字典
#
# dict2 = {
#     "name": "李四",
#     "ww": "ww"
# }
# dict1.update(dict2)  # 升级字典   如果key存在就修改   不存在就添加
#
# keys = dict1.keys()   #   获取字典中所有key
# vaules = dict1.values()   # 获取所有的值
# items = dict1.items()     #  获取字典中的所有键值对
# for key, value in dict1.items():
#     print(key)
#     print(value)                            #  获取所有  键   值
#
# for key in dict1.keys():
#     print(key)
# list = list(keys)
# print(sys.getsizeof(list))
# print(sys.getsizeof(keys))
#
# for xx in dict1:     #直接遍历字典得到的是key
#     print(dict1[xx])