import pygame


class Ship(object):
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # 获取图片矩形
        self.screen_rect = screen.get_rect()  # 获取屏幕矩形
        # 设置矩形位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

    def update(self):
        # 正在移动且没有超出边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):  # 绘制飞船
        self.screen.blit(self.image, self.rect)
