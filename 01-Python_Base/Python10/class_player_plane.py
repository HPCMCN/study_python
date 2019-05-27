import pygame  # 导入包  里面都是动态模块不需要加文件名  动态模块名字格式.dll, .pyd
from Python10.class_bullet import Bullet


class Player_plane:
    """玩家飞机"""
    def __init__(self, img_path, x, y, window):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = window
        self.bullets = []

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def move_left(self):
        if self.x > -50:
            self.x -= 20

    def move_right(self):
        if 462 > self.x:
            self.x += 20

    def move_up(self):
        if self.y > -25:
            self.y -= 20

    def move_down(self):
        if 743 > self.y:
            self.y += 20

    def fire(self):
        bullet = Bullet(r"res\bullet_12.png", self.x, self.y, self.window)
        self.bullets.append(bullet)

    def display_bullet(self):
        a = 0
        for num in range(len(self.bullets)):
            if self.bullets[num - a].y > -50:
                self.bullets[num - a].display()
                self.bullets[num - a].move_up()
            else:
                self.bullets.remove(self.bullets[num - a])
                a += 1

    def died(self):
        pass
