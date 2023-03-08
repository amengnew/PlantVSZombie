import sys
import traceback

import pygame
from pygame.locals import *

import SeedBank

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


    # 菜单界面
    open_menu = False
    menu_image = pygame.image.load("photo/others/menu.png").convert_alpha()
    menu_rect = menu_image.get_rect()
    menu_rect.centerx, menu_rect.centery = width // 2, height // 2
    button_nor_image = pygame.image.load("photo/others/button_nor.png").convert_alpha()
    button_pressed_image = pygame.image.load("photo/others/button_pressed.png").convert_alpha()
    button_image = button_nor_image
    button_rect = button_image.get_rect()
    button_rect.right, button_rect.top = width, 0
    resume_nor_image = pygame.image.load("photo/others/resume_nor.png").convert_alpha()
    resume_pressed_image = pygame.image.load("photo/others/resume_pressed.png").convert_alpha()
    resume_image = resume_nor_image
    resume_rect = resume_image.get_rect()
    resume_rect.left, resume_rect.top = 298, 408
    check_box_image = pygame.image.load("photo/others/check_box.png").convert_alpha()
    check_box_rect1 = check_box_image.get_rect()
    check_box_rect2 = check_box_image.get_rect()
    check_box_rect1.centerx, check_box_rect1.centery = 450, 260
    check_box_rect2.centerx, check_box_rect2.centery = 450, 297
    tick_image = pygame.image.load("photo/others/tick.png").convert_alpha()
    tick_rect1 = tick_image.get_rect()
    tick_rect2 = tick_image.get_rect()
    tick_rect1.centerx, tick_rect1.centery = check_box_rect1.centerx, check_box_rect1.centery
    tick_rect2.centerx, tick_rect2.centery = check_box_rect2.centerx, check_box_rect2.centery
    quitgame_nor_image = pygame.image.load("photo/others/quitgame_nor.png").convert_alpha()
    quitgame_pressed_image = pygame.image.load("photo/others/quitgame_pressed.png").convert_alpha()
    quitgame_image = quitgame_nor_image
    quitgame_rect = quitgame_image.get_rect()
    quitgame_rect.left, quitgame_rect.top = 318, 352

    # 游戏界面
    bg_image = pygame.image.load("photo/others/background.png").convert_alpha()
    bg_rect = bg_image.get_rect()
    bg_rect.left, bg_rect.top = -200, 0
    bar_image = pygame.image.load("photo/others/FlagMeterEmpty.png").convert_alpha()
    bar_parts1_image = pygame.image.load("photo/others/FlagMeterParts1.png").convert_alpha()
    bar_parts2_image = pygame.image.load("photo/others/FlagMeterParts2.png").convert_alpha()
    largewave_image = pygame.image.load("photo/others/LargeWave.gif").convert_alpha()
    largewave_rect = largewave_image.get_rect()
    largewave_rect.centerx, largewave_rect.centery = width // 2, height // 2
    seedbank = SeedBank.SeedBank()

    # 游戏是否结束
    gameover = False

    # 游戏进度条长度
    bar_length = 1

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 菜单操作
            if event.type == MOUSEBUTTONDOWN:
                if not gameover and start_ready:
                    if event.button == 1 and button_rect.collidepoint(event.pos):
                        open_menu = True
                    if event.button == 1 and quitgame_rect.collidepoint(event.pos) and open_menu:
                        pygame.quit()
                        sys.exit()
                if not gameover:
                    if event.button == 1 and resume_rect.collidepoint(event.pos):
                        open_menu = False

                # 游戏初始界面操作,按键反射
                if not start:
                    if event.button == 1 and start_rect.collidepoint(
                            event.pos) and not open_menu and not open_help:
                        start = True
                    if event.button == 1 and exit_rect.collidepoint(
                            event.pos) and not open_menu and not open_help:
                        pygame.quit()
                        sys.exit()
                    if event.button == 1 and help_rect.collidepoint(event.pos) and not open_menu:
                        open_help = True
                    if event.button == 1 and off_help__rect.collidepoint(event.pos) and open_help:
                        open_help = False
                    if event.button == 1 and option_rect.collidepoint(event.pos) and not open_help:
                        open_menu = True

            # 初始界面按键高亮
            elif event.type == MOUSEMOTION:
                # 所以button的按压样式
                if button_rect.collidepoint(event.pos) and not open_menu:
                    button_image = button_pressed_image
                else:
                    button_image = button_nor_image
                if resume_rect.collidepoint(event.pos) and open_menu:
                    resume_image = resume_pressed_image
                else:
                    resume_image = resume_nor_image
                if quitgame_rect.collidepoint(event.pos) and start_ready:
                    quitgame_image = quitgame_pressed_image
                else:
                    quitgame_image = quitgame_nor_image
                # if quit_rect.collidepoint(event.pos) and gameover:
                #     quit_image = quit_pressed_image
                # else:
                #     quit_image = quit_nor_image
                if start_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    start_image = start_pressed_image
                else:
                    start_image = start_nor_image
                if exit_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    exit_image = exit_pressed_image
                else:
                    exit_image = exit_nor_image
                if help_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    help_image = help_pressed_image
                else:
                    help_image = help_nor_image
                if option_rect.collidepoint(event.pos) and not start and not open_menu and not open_help:
                    option_image = option_pressed_image
                else:
                    option_image = option_nor_image




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
        else:
            screen.blit(bg_image, bg_rect)

            if not gameover:
                # 绘制游戏进度条
                if start_ready:
                    screen.blit(bar_image, (width - 200, height - 27))
                    screen.blit(bar_parts2_image, (width - 195, height - 30))
                    pygame.draw.line(screen, BAR_COLOR, (width - 51 - bar_length, height - 17),
                                     (width - 51, height - 17), 7)
                    screen.blit(bar_parts1_image, (width - 68 - bar_length, height - 32))

                # 绘制卡片栏
                if not open_menu and not gameover:
                    seedbank.move()
                screen.blit(seedbank.image, seedbank.rect)
                # 绘制卡片栏里的卡片
                # if seedbank.position:
                #     for px in plantx:
                #         screen.blit(px.card_image, px.card_rect)

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