class SweetPotato:

    def __init__(self, name):
        self.name = name
        self.state = "生的"
        self.cooked_time = 0
        self.condiment = []

    def cook(self, time):
        self.cooked_time += time
        if 0 <= self.cooked_time < 3:
            self.state = "生的"
        elif 3 <= self.cooked_time < 6:
            self.state = "快熟了,再等会"
        elif 6 <= self.cooked_time < 9:
            self.state = "熟了"
        else:
            self.state = "糊了"

    def add_condiment(self, condiment):
        self.condiment.append(condiment)

    def __str__(self):
        return "\n\n地瓜%s状态是: %s\n调料添加情况: %s \n烧烤时间为: %d" % (self.name, self.state, self.condiment, self.cooked_time)


dg1 = SweetPotato(1)
dg2 = SweetPotato(2)
print(dg1, dg2)
dg1.cook(3)
dg2.cook(3)
dg1.add_condiment("可乐")
dg2.add_condiment("可乐")
print(dg1, dg2)
dg1.cook(9)
dg2.cook(9)
dg1.add_condiment("辣椒")
dg2.add_condiment("辣椒")
print(dg1, dg2)
