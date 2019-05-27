class Meat:
    """肉类"""

    def __init__(self, name):
        self.name = name


class Ham(Meat):
    """火腿类"""
    pass


class SweetPotato:

    def __init__(self):
        self.name = "地瓜"


class Person:

    def __init__(self):
        self.name = "超哥"

    def eat(self, meat):
        print("%s 要吃 %s" % (self.name, meat.name))


m1 = Meat("黑猪肉")
print(m1)
h1 = Ham("火腿")

dg = SweetPotato()

cg = Person()
cg.eat(m1)
