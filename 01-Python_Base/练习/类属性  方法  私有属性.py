import random
# class Play:
#     def __init__(self, number=1, type_date="其他"):
#         self.price = 100
#         self.number = number
#         self.type_date = type_date
#     def true_price(self):
#         if self.type_date =="周末":
#             self.price = 100 * 1.2 * self.number
#         elif self.type_date =="儿童":
#             self.price = 100 * 0.5 * self.number
#         else:
#             self.price = 100 * self.number
#         return print(self.price)
#
#
# a = Play(number=1, type_date="儿童")
# a.true_price()
# c = Play(number=2)
# c.true_price()
# print(a.price + c.price)


class Gui:
    """乌龟类"""
    def __init__(self):
        self.hp = 100
        self.x = 0
        self.y = 0

    def move(self):
        if self.x in range(11) and self.y in range(11):
            print("移动2")
            self.x += random.randint(1, 2)
            self.y += random.randint(1, 2)

        else:
            self.x += random.randint(1, 2)
            self.y += random.randint(1, 2)
        self.hp -= 1
        self.died()

    def died(self):
        if self.hp <= 0:
            return None
        else:
            return True

    def re_hp(self, fish):
        if self.x == fish.x and self.y == fish.y:
            self.hp += 20
            if self.hp > 100:
                self.hp = 100
            return None
        else:
            return True


class Fish:
    """鱼类"""
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        if self.x in range(11) and self.y in range(11):
            print("移动1")
            self.x += 1
            self.y += 1

    def died(self, gui, fish):
        if gui.re_hp():
            pass
        else:
            del fish


if __name__ == '__main__':
    pass
