import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()  # 引入设置类
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 设置宽高
    screen.fill(ai_settings.bg_color)  # 设置背景色
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)  # 飞船类

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ship.blitme()  # 绘制飞船
        pygame.display.flip()  # 让最近绘制的屏幕可见


run_game()
