import sys
import pygame
import time

import game_functions as gfunc
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储统计信息的实例
    stats = GameStats(ai_settings)
    sboard = Scoreboard(ai_settings, screen, stats)

    # 创造一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = pygame.sprite.Group()

    # 创建外星人
    aliens = pygame.sprite.Group()
    gfunc.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gfunc.check_event(ai_settings, screen, stats, sboard, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gfunc.update_bullets(ai_settings, screen, stats, sboard, ship, aliens, bullets)
            gfunc.update_aliens(ai_settings, stats, sboard, screen, ship, aliens, bullets)

        gfunc.update_screen(ai_settings, screen, stats, sboard, ship, aliens, bullets, play_button)
        # print('updated: ' + str(time.time()))


run_game()
