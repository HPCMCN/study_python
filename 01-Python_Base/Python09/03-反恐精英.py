# 警察土匪                                                  枪子弹
# 创建一个类 丢警察和土匪                                创建一个枪的类
# 属性包括  mane 血量  枪支                       属性 name  子弹数量  伤害
# 方法   射击  血量减少  判断死亡             方法  子弹减少  判断是否有子弹   子弹填充


class Gun:
    """枪类"""

    def __init__(self, model, damage, count):
        self.model = model
        self.damage = damage
        self.bullet_count = count
        self.count = 2

    def add_bullet(self, count):
        """添加子弹"""
        self.bullet_count += count

    def shoot(self, enemy):
        """射击"""
        if self.bullet_count:
            self.bullet_count -= 1
            enemy.hurt(self.damage)
        else:
            print("请添加子弹")
            cmd = input("是否添加子弹:\n1.是\n2.否")
            if cmd == "1":
                self.add_bullet(self.count)

    def __str__(self):
        return "型号为: %s\n伤害: %s\n子弹剩余: %s\n" % (self.model, self.damage, self.bullet_count)


class Player:
    """创建玩家"""

    def __init__(self, name, gun):
        self.name = name
        self.hp = 100
        self.gun = gun
        self.state = "存活"

    def fire(self, enemy):
        if self.gun:
            self.gun.shoot(enemy)
        else:
            print("请用目光杀死他")

    def hurt(self, enemy_gun):
        self.hp = self.hp - enemy_gun
        if self.hp > 0:
            print("%s已中枪\n" % self.name)
        else:
            print("玩家%s已经阵亡\n" % self.name)
            self.hp = 0
            self.state = "死亡"

    def __str__(self):
        return "玩家:%s, 武器:%s,\n当前状态:%s, 剩余子弹:%s, 当前血量:%s\n" % \
               (self.name, self.gun.model, self.state, self.gun.bullet_count, self.hp)


gun1 = Gun(None, None, None)
player1 = Player("土匪", gun1)
print(player1)

gun2 = Gun("火箭炮", 1000, 2)
player2 = Player("cg", gun2)
print(player2)

player1.fire(player2)
print(player2)

player2.fire(player1)
print(player1)
print(player2)

player2.fire(player1)
print(player1)
print(player2)

player2.fire(player1)
print(player1)
print(player2)
