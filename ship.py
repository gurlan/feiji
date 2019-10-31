import pygame


class Ship(object):
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # 获取图片矩形
        self.screen_rect = screen.get_rect()  # 获取屏幕矩形
        # 设置矩形位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect) #绘制飞船

