import sys
import traceback

import pygame
from pygame.locals import *

# pygame初始化
pygame.init()
pygame.mixer.init()

# 创建窗口大小
bg_size = width, height = 800, 600
screen = pygame.display.set_mode(bg_size)

pygame.display.set_caption("植物大战僵尸-头歌")
clock = pygame.time.Clock()

# 颜色
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BAR_COLOR = (189, 223, 89)

# 植物种植范围
borderx = L, R = 30, 780
bordery = T, B = 90, 570
X = [75, 155, 235, 322, 406, 480, 562, 641, 720]
Y = [135, 225, 325, 427, 523]


def main():
    # 游戏开始界面
    start = False
    start_ready = False
    open_help = False
    start_bg_image = pygame.image.load("photo/others/start_background.png").convert_alpha()
    start_nor_image = pygame.image.load("photo/others/start_nor.png").convert_alpha()
    start_pressed_image = pygame.image.load("photo/others/start_pressed.png").convert_alpha()
    start_image = start_nor_image
    start_rect = start_image.get_rect()
    start_rect.left, start_rect.top = 467, 86
    game_logo_image = pygame.image.load("photo/others/game_logo.png").convert_alpha()
    game_logo_rect = game_logo_image.get_rect()
    game_logo_rect.left, game_logo_rect.top = 13, -game_logo_rect.height
    exit_nor_image = pygame.image.load("photo/others/exit_nor.png").convert_alpha()
    exit_pressed_image = pygame.image.load("photo/others/exit_pressed.png").convert_alpha()
    exit_image = exit_nor_image
    exit_rect = exit_image.get_rect()
    exit_rect.left, exit_rect.top = 730, 515
    help_nor_image = pygame.image.load("photo/others/help_nor.png").convert_alpha()
    help_pressed_image = pygame.image.load("photo/others/help_pressed.png").convert_alpha()
    help_image = help_nor_image
    help_rect = help_image.get_rect()
    help_rect.left, help_rect.top = 667, 526
    option_nor_image = pygame.image.load("photo/others/option_nor.png").convert_alpha()
    option_pressed_image = pygame.image.load("photo/others/option_pressed.png").convert_alpha()
    option_image = option_nor_image
    option_rect = option_image.get_rect()
    option_rect.left, option_rect.top = 607, 489
    help_doc_image = pygame.image.load("photo/others/Help.png").convert_alpha()
    help_doc_rect = help_doc_image.get_rect()
    help_doc_rect.centerx, help_doc_rect.centery = width // 2, height // 2
    off_help_image = pygame.image.load("photo/others/off_help.png").convert_alpha()
    off_help__rect = off_help_image.get_rect()
    off_help__rect.left, off_help__rect.top = 615, 120
    prepare_tip_images = []
    prepare_tip_images.extend([
        pygame.image.load("photo/others/PrepareGrowPlants1.png").convert_alpha(),
        pygame.image.load("photo/others/PrepareGrowPlants2.png").convert_alpha(),
        pygame.image.load("photo/others/PrepareGrowPlants3.png").convert_alpha()
    ])
    prepare_tip_rect = prepare_tip_images[0].get_rect()
    prepare_tip_rect.centerx, prepare_tip_rect.centery = width // 2, height // 2
    index_prepare_tip_image = -1

    gameover = False


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not start:
            # 绘制游戏初始界面
            pygame.mixer.music.pause()
            screen.blit(start_bg_image, (0, 0))
            screen.blit(game_logo_image, game_logo_rect)
            game_logo_rect.top += 10
            if game_logo_rect.top > 8:
                game_logo_rect.top = 8
            screen.blit(start_image, start_rect)
            screen.blit(exit_image, exit_rect)
            screen.blit(help_image, help_rect)
            screen.blit(option_image, option_rect)
            if open_help:
                screen.blit(help_doc_image, help_doc_rect)
                screen.blit(off_help_image, off_help__rect)

        pygame.display.flip()
        clock.tick(60)  # 游戏帧率



if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()