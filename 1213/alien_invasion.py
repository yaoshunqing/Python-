# @Time : 2020/5/2 8:58 
# @Author : Yao
# @File : alien_invasion.py 
# @Software: PyCharm

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    # 设置屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)
        # pygame.time.delay(1)


run_game()
