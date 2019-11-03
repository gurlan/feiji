import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()  # 初始化
    ai_settings = Settings()  # 引入设置类
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 设置宽高
    pygame.display.set_caption("Alien Invasion")  # 设置游戏名称
    ship = Ship(screen, ai_settings)  # 飞船类

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)  # 监听键盘和鼠标事件
        ship.update()
        gf.update_screen(ai_settings, screen, ship)  # 绘制屏幕


run_game()
