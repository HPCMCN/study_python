# 让new只走一次   防止重新定以实例对象
class ShoppingCart:
    """购物车"""
    __instance = None  # 定义两个私有类属性  用来判断是否已经创建过对象和属性
    __has_init = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return ShoppingCart.__instance

    def __init__(self):
        if ShoppingCart.__has_init is False:
            self.total_price = 200
            ShoppingCart.__has_init = True


cart1 = ShoppingCart()
cart2 = ShoppingCart()
print(cart2.total_price)
print(cart1)
cart1.total_price = 0
print(cart1.total_price)
print(cart2.total_price)
print(cart2)
