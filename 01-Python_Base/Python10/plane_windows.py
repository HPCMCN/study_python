import pygame  # 导入包  里面都是动态模块不需要加文件名  动态模块名字格式.dll, .pyd
import sys
from pygame.locals import *
import random
import time


class Img:
    """导入地图"""
    def __init__(self, img_path, x, y, windows):
        self.img = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.window = windows

    def display(self):
        self.window.blit(self.img, (self.x, self.y))


class Bullet(Img):
    """子弹类"""
    def display(self):
        self.window.blit(self.img, (self.x + 40, self.y))

    def move_up(self, sum2):
        self.y -= 40
        if sum2 == 0:
            pass
        elif sum2 == 1:
            self.x -= 10
        elif sum2 == 2:
            self.x -= 20
        elif sum2 == 3:
            self.x -= 30
        elif sum2 == 4:
            self.x -= 40
        elif sum2 == 5:
            self.x += 10
        elif sum2 == 6:
            self.x += 20
        elif sum2 == 7:
            self.x += 30
        elif sum2 == 8:
            self.x += 40

    def __del__(self):
        print("检测子弹是否被释放了")

    def died(self, enemy_plane1):
        if enemy_plane1.x <= self.x <= (enemy_plane1.x+100) and enemy_plane1.y <= self.y <= (enemy_plane1.y+50):
            return 0, enemy_plane1
        else:
            pass


class EnemyBullet(Img):
    """敌机子弹"""
    def display(self):
        self.window.blit(self.img, (self.x + 40, self.y))

    def move_down(self):
        self.y += 15

    def __del__(self):
        print("检测子弹是否被释放了")

    def died(self, player_plane1):
        if player_plane1.x <= self.x <= (player_plane1.x+100) and player_plane1.y <= self.y <= (player_plane1.y+50):
            return 0
        else:
            pass


class Enemy_plane(Img):
    """敌机"""
    def __init__(self, img_nb, x, y, windows):
        self.img_nb = img_nb
        super(Enemy_plane, self).__init__("res/img-plane_%d.png" % self.img_nb, x, y, windows)
        self.b = 0
        self.c = 0
        self.enemy_bullet = []

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

    def display_bullet(self, player_plane1):
        a = 0
        for enemy_bullet_n in range(len(self.enemy_bullet)):
            if self.enemy_bullet[enemy_bullet_n - a].y > 800:
                self.enemy_bullet.remove(self.enemy_bullet[enemy_bullet_n - a])
                a += 1
            else:
                self.enemy_bullet[enemy_bullet_n - a].display()
                self.enemy_bullet[enemy_bullet_n - a].move_down()
                m = self.enemy_bullet[enemy_bullet_n - a].died(player_plane1)
                if m == 0:
                    return 0

    def died(self):
        player_plane.fire()


class Player_plane(Img):
    """玩家飞机"""
    def __init__(self, img_path, x, y, windows):
        super().__init__(img_path, x, y, windows)
        self.bullets = []

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
        for _ in range(9):
            bullet = Bullet(r"res\bullet_12.png", self.x, self.y, self.window)
            self.bullets.append(bullet)

    def display_bullet(self):
        a = 0
        for num in range(len(self.bullets)):
            if self.bullets[num - a].y > -50:
                self.bullets[num - a].display()
                self.bullets[num - a].move_up((num-a) % 9)
                m = self.bullets[num - a].died(enemy_plane)
                if m == 0:
                    self.bullets.remove(self.bullets[num - a])
                    a += 1
                    return True

            else:
                self.bullets.remove(self.bullets[num - a])
                a += 1


window = pygame.display.set_mode((512, 768))  # 创建窗口

bg_img = Img(r"res\img_bg_level_1.jpg", 0, 0, window)  # 导入背景

player_plane = Player_plane(r"res\hero.png", 206, 600, window)  # 导入玩家飞机
enemy_list = []

for _ in range(5):
    enemy_plane = Enemy_plane(random.randint(1, 7), random.randint(-51, 462),
                              random.randint(-300, -100), window)
    enemy_list.append(enemy_plane)

num1 = 0
cmd = 1
while True:

    bg_img.display()  # 背景贴图

    player_plane.display()

    player_plane.display_bullet()

    for enemy_plane in enemy_list:
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.judge()
        if num1 % 10 == 1:
            enemy_plane.enemy_fire()
        cmd = enemy_plane.display_bullet(player_plane)
        if cmd == 0:
            break
    if cmd == 0:
            break
    pygame.display.update()  # 刷新窗口

    for event in pygame.event.get():  # 检测时间

        if event.type == QUIT:  # 获取点击关闭窗口时间

            sys.exit()


    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
        print("left")
        player_plane.move_left()

    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        print("right")
        player_plane.move_right()

    if pressed_keys[K_w] or pressed_keys[K_UP]:
        print("up")
        player_plane.move_up()

    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
        print("down")
        player_plane.move_down()

    if pressed_keys[K_SPACE]:
        print("space")
        if num1 % 3 == 1:
            player_plane.fire()

    num1 += 1

    time.sleep(0.05)
