class Furniture:
    """家具类"""
    def __init__(self, type1, area):
        self.type = type1  # 家具类型
        self.area = area  # 占地面积

    def __str__(self):
        return "家具类型: %s, 占地面积: %d" % (self.type, self.area)


class Home:
    """房子"""
    def __init__(self, address):
        self.address = address
        self.area = 200
        self.free_area = 200

    def add_furniture(self, furniture):
        if self.free_area >= furniture.area:
            print("%s家具添加成功" % furniture.type)
            self.free_area -= furniture.area
        else:
            print("%s家具添加失败")

    def __str__(self):
        return "地址: %s\n占地面积: %s m³\n剩余面积: %s m³" % (self.address, self.area, self.free_area)


bed = Furniture("床", 4)
print(bed)
yc = Furniture("泳池", 196)
print(yc)

home1 = Home("独家小院")
home1.add_furniture(bed)
home1.add_furniture(yc)
print(home1)
