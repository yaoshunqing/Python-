# @Time : 2020/5/2 17:08 
# @Author : Yao
# @File : game_functions.py 
# @Software: PyCharm

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # q键关闭游戏
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #尝试删掉screen
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹位置并删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        # 这个.copy()加不加似乎不影响
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #检查是否有子弹击中
    #如果是这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 新增这行代码遍历bullets中的每颗子弹，再遍历编组aliens中外星人。每当有子弹和外星人的rect重叠时，groupcollide()就在它返回
    # 的字典中添加一个键值对。两个实际参数True告诉pygame删除发生碰撞的子弹和外星人
    print(len(aliens))
    #删除现有的子弹并新建一群外星人
    if len(aliens) == 0:
        bullets.empty()
        print("hoo")
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    # 子弹数目不能超过设置中的最大数目
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y =  (ai_settings.screen_height -
                          (3 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



def update_aliens(ai_settings, aliens):
    """检查是否有外星人位于屏幕边缘，并更新外星人群中外星人位置"""

    check_fleet_edges(ai_settings, aliens)
    aliens.update()


