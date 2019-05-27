class Father:
    """father类"""
    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1

    def get_name(self):
        print("name is %s" % self.name)

    def get_age(self):
        print("age is %s" % self.age)


class Son(Father):
    """son类"""
    def get_name(self):
        print("name is %s\nage is %s" % (self.name, self.age))


name1 = Son("小明", 18)
name1.get_age()
name1.get_name()
