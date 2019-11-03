import sys
import pygame


def check_events(ship):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 退出事件
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 按键盘事件
            keydown(ship, event)
        elif event.type == pygame.KEYUP:  # 抬起键盘事件
            keyup(ship, event)


def keydown(ship, event):
    if event.key == pygame.K_RIGHT:  # 如果是右方向键
        ship.moving_right = True
    if event.key == pygame.K_LEFT:  # 如果是左方向键
        ship.moving_left = True


def keyup(ship, event):
    if event.key == pygame.K_RIGHT:  # 如果是右方向键
        ship.moving_right = False
    if event.key == pygame.K_LEFT:  # 如果是左方向键
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)  # 荧幕背景色
    ship.blitme()  # 绘制飞船
    pygame.display.flip()  # 绘制荧幕
