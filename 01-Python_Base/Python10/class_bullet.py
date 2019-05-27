import pygame  # 导入包  里面都是动态模块不需要加文件名  动态模块名字格式.dll, .pyd
from Python10.plane_windows import player_plane


class Bullet:
    """子弹类"""
    def __init__(self, img_nb, x, y, window):
        self.img = pygame.image.load(img_nb)
        self.img1 = pygame.image.load(img_nb)
        self.img2 = pygame.image.load(img_nb)
        self.img3 = pygame.image.load(img_nb)
        self.img4 = pygame.image.load(img_nb)
        self.img5 = pygame.image.load(img_nb)
        self.img6 = pygame.image.load(img_nb)
        self.img7 = pygame.image.load(img_nb)
        self.img8 = pygame.image.load(img_nb)
        self.x = x
        self.y = y
        self.window = window

    def display(self):
        self.window.blit(self.img, (self.x + 40, self.y))
        self.window.blit(self.img1, (self.x + 10, self.y))
        self.window.blit(self.img2, (self.x - 20, self.y))
        self.window.blit(self.img3, (self.x - 50, self.y))
        self.window.blit(self.img4, (self.x - 80, self.y))
        self.window.blit(self.img5, (self.x + 70, self.y))
        self.window.blit(self.img6, (self.x + 100, self.y))
        self.window.blit(self.img7, (self.x + 130, self.y))
        self.window.blit(self.img8, (self.x + 160, self.y))

    def move_up(self):
        self.y -= 40


    def __del__(self):
        print("检测子弹是否被释放了")

    # def die(self):
    #     if self.x == player_plane.x and self.y == player_plane.y:
    #         del player_plane


class EnemyBullet:
    """敌机子弹"""
    def __init__(self, img_nb, x, y, window):
        self.img = pygame.image.load(img_nb)
        self.x = x
        self.y = y
        self.window = window

    def display(self):
        self.window.blit(self.img, (self.x + 40, self.y))

    def move_down(self):
        self.y += 15

    def __del__(self):
        print("检测子弹是否被释放了")
