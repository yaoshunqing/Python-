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
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    # 设置屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #background = pygame.image.load_basic('images/alien.bmp').convert()
    pygame.display.set_caption("Alien Invasion")


    # # 添加背景图片
    # background = pygame.image.load_extended('images/universe.jpg').convert()
    # screen.blit(background, (0, 0))

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)


    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens,bullets)
        # pygame.time.delay(1)


run_game()
