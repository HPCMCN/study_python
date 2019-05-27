import pygame  # 导入包  里面都是动态模块不需要加文件名  动态模块名字格式.dll, .pyd
import random
from Python10.class_bullet import EnemyBullet


class Enemy_plane:
    """敌机"""
    def __init__(self, img_nb, x, y, window):
        self.img_nb = img_nb
        self.img = pygame.image.load("res/img-plane_%d.png" % self.img_nb)
        self.x = x
        self.y = y
        self.window = window
        self.b = 0
        self.c = 0
        self.enemy_bullet = []

    def display(self):
        self.window.blit(self.img, (self.x, self.y))

    def move(self):
        if self.img_nb % 3 == 0:

            self.y += 3

        elif self.img_nb % 3 == 1:

            self.y += 3

            if self.x <= 462 and self.c == 0:
                self.x += 3
                if self.x > 462:
                    self.c = 1
            else:
                self.x -= 2
                if self.x < -50:
                    self.c = 0

        elif self.img_nb % 3 == 2:

            self.y += 3
            if self.x >= -50 and self.b == 0:
                self.x -= 3
                if self.x < -50:
                    self.b = 1
            else:
                self.x += 2
                if self.x > 462:
                    self.b = 0

    def judge(self):
        if self.y > 836:
            self.y = random.randint(-300, -100)
            self.x = random.randint(-51, 462)
            self.img_nb = random.randint(1, 7)

    def enemy_fire(self):
        if self.y > -93:
            enemy_bullet = EnemyBullet(r"res\bullet_1.png", self.x, self.y + 50, self.window)
            self.enemy_bullet.append(enemy_bullet)

    def display_bullet(self):
        a = 0
        for enemy_bullet_n in range(len(self.enemy_bullet)):
            if self.enemy_bullet[enemy_bullet_n - a].y > 800:
                self.enemy_bullet.remove(self.enemy_bullet[enemy_bullet_n - a])
                a += 1
            else:
                self.enemy_bullet[enemy_bullet_n - a].display()
                self.enemy_bullet[enemy_bullet_n - a].move_down()

    def died(self):
        pass