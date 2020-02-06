# -*- coding: utf-8 -*-
import os
import sys
import pygame
import math
import random
from pygame.locals import *

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if colorkey is None:
        image = pygame.image.load(fullname).convert()
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = pygame.image.load(fullname).convert()
    return image


def get(name):
    fullname = os.path.join('data', name)
    return fullname


def buttons(name):
    image = pygame.transform.scale(load_image(name), (300, 100))
    return image


# #комменты будем писать так, а нерабочие или ненужные строки с одной решоткой

def game_intro():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    DARK_RED = (200, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 200, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    LIGHT_GREEN = (114, 230, 24)
    BLOOD = (204, 0, 0)
    DARK_BLUE = (0, 0, 153)
    BROWN = (152, 85, 2)
    FIRST_BUTTON1 = (156, 140, 162)
    FIRST_BUTTON2 = (188, 140, 205)
    # #эти можешь попробовать, но мы будем использовать fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # screen = p
    # pygame.display.set_mode((400, 400), RESIZEABLE)
    # screen = pygame.display.set_mode((400, 400))
    size = window_width, window_height = screen.get_width(), screen.get_height()
    pygame.display.set_caption('De Life')  # #название игры нужно придумать и поменять это

    background = pygame.transform.scale(load_image('fon.png', 1), (window_width, window_height))
    family = pygame.transform.scale(load_image('family.png'), (256, 256))
    logo = pygame.transform.scale(load_image('logo.png'), (64, 64))
    kursor = pygame.transform.scale(load_image("cursor.png"), (40, 40))
    music = "Main_Theme.mp3"
    pygame.mixer.music.load(get(music))
    pygame.mixer.music.play(-1, 0)

    # #это будут надписи типа "made by ...", правили и название. Твоя работа
    # font = pygame.font.SysFont('Arial', 72)
    # text = font.render("Hello", True, WHITE)
    # screen.blit(text, (30, 30))

    # #кнопки
    xStartGame = int(window_width / 15)
    yStartGame = int(window_height / 20)
    startImage = buttons("startGame1.png")

    xContinue = int(window_width / 15)
    yContinue = int(window_height / 20) + 100

    xOptions = int(window_width / 15)
    yOptions = int(window_height / 20) + 200

    screen.blit(background, (0, 0))
    screen.blit(startImage, (xStartGame, yStartGame))

    xExit = int(window_width / 15)
    yExit = int(window_height / 20) + 300
    screen.blit(family, (700, 20))
    screen.blit(logo, (1250, 650))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                screen.blit(background, (0, 0))
                screen.blit(startImage, (xStartGame, yStartGame))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if xStartGame < mouse[0] < xStartGame + 367 and yStartGame < mouse[1] < yStartGame + 96:
                startImage = buttons("startGame2.png")
                screen.blit(startImage, (xStartGame, yStartGame))
                if click[0] == 1:
                    first_round()
            else:
                startImage = buttons("startGame1.png")
                screen.blit(startImage, (xStartGame, yStartGame))
            if xContinue < mouse[0] < xContinue + 220 and yContinue < mouse[1] < yContinue + 95:
                continueImage = buttons("continue2.png")
                screen.blit(continueImage, (xContinue, yContinue))
                if click[0] == 1:
                    my_file = open('save.txt', 'r')
                    my_string = my_file.read()
                    my_file.close()
                    if my_string == '':
                        first_round()
                    else:
                        my_string
            else:
                continueImage = buttons("continue1.png")
                screen.blit(continueImage, (xContinue, yContinue))
            if xOptions < mouse[0] < xOptions + 220 and yOptions < mouse[1] < yOptions + 95:
                optionsImage = buttons("options2.png")
                screen.blit(optionsImage, (xOptions, yOptions))
                if click[0] == 1:
                    options()
            else:
                optionsImage = buttons("options1.png")
                screen.blit(optionsImage, (xOptions, yOptions))
            if xExit < mouse[0] < xExit + 212 and yExit < mouse[1] < yExit + 95:
                exitImage = buttons("quit2.png")
                screen.blit(exitImage, (xExit, yExit))
                if click[0] == 1:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
            else:
                exitImage = buttons("quit1.png")
                screen.blit(exitImage, (xExit, yExit))
            screen.blit(family, (700, 20))
            screen.blit(logo, (1250, 650))
            screen.blit(kursor, mouse)
            pygame.display.update()


def wm():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    size = window_width, window_height = screen.get_width(), screen.get_height()
    pygame.display.set_caption('De Life')  # #название игры нужно придумать и поменять это

    background = pygame.transform.scale(load_image('fon.png', 1), (window_width, window_height))
    family = pygame.transform.scale(load_image('family.png'), (256, 256))
    logo = pygame.transform.scale(load_image('logo.png'), (64, 64))
    kursor = pygame.transform.scale(load_image("cursor.png"), (40, 40))
    xStartGame = int(window_width / 15)
    yStartGame = int(window_height / 20)
    startImage = buttons("startGame1.png")

    xContinue = int(window_width / 15)
    yContinue = int(window_height / 20) + 100

    xOptions = int(window_width / 15)
    yOptions = int(window_height / 20) + 200

    screen.blit(background, (0, 0))
    screen.blit(startImage, (xStartGame, yStartGame))

    xExit = int(window_width / 15)
    yExit = int(window_height / 20) + 300
    screen.blit(family, (700, 20))
    screen.blit(logo, (1250, 650))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                screen.blit(background, (0, 0))
                screen.blit(startImage, (xStartGame, yStartGame))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if xStartGame < mouse[0] < xStartGame + 367 and yStartGame < mouse[1] < yStartGame + 96:
                startImage = buttons("startGame2.png")
                screen.blit(startImage, (xStartGame, yStartGame))
                if click[0] == 1:
                    first_round()
            else:
                startImage = buttons("startGame1.png")
                screen.blit(startImage, (xStartGame, yStartGame))
            if xContinue < mouse[0] < xContinue + 220 and yContinue < mouse[1] < yContinue + 95:
                continueImage = buttons("continue2.png")
                screen.blit(continueImage, (xContinue, yContinue))
                if click[0] == 1:
                    my_file = open('save.txt', 'r')
                    my_string = my_file.read()
                    my_file.close()
                    if my_string == '':
                        first_round()
                    else:
                        my_string
            else:
                continueImage = buttons("continue1.png")
                screen.blit(continueImage, (xContinue, yContinue))
            if xOptions < mouse[0] < xOptions + 220 and yOptions < mouse[1] < yOptions + 95:
                optionsImage = buttons("options2.png")
                screen.blit(optionsImage, (xOptions, yOptions))
                if click[0] == 1:
                    options()
            else:
                optionsImage = buttons("options1.png")
                screen.blit(optionsImage, (xOptions, yOptions))
            if xExit < mouse[0] < xExit + 212 and yExit < mouse[1] < yExit + 95:
                exitImage = buttons("quit2.png")
                screen.blit(exitImage, (xExit, yExit))
                if click[0] == 1:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()
            else:
                exitImage = buttons("quit1.png")
                screen.blit(exitImage, (xExit, yExit))
            screen.blit(family, (700, 20))
            screen.blit(logo, (1250, 650))
            screen.blit(kursor, mouse)
            pygame.display.update()


def options():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    size = window_width, window_height = screen.get_width(), screen.get_height()
    background = pygame.transform.scale(load_image('fon.png', 1), (window_width, window_height))
    pygame.display.set_caption('De Life')  # #название игры нужно придумать и поменять это
    voice = load_image("voice.png", 1)
    back = load_image("back.png")
    screen.blit(voice, (700, 20))
    screen.blit(back, (100, 20))
    background = pygame.transform.scale(load_image('fon.png', 1), (window_width, window_height))
    kursor = pygame.transform.scale(load_image("cursor.png"), (40, 40))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                screen.blit(background, (0, 0))
                screen.blit(voice, (500, 200))
                screen.blit(back, (100, 20))
            mouse = pygame.mouse.get_pos()
            if 500 < mouse[0] < 700 and 200 < mouse[1] < 300:
                if click[0] == 1:
                    pygame.mixer.music.stop()
            if 100 < mouse[0] < 200 and 20 < mouse[1] < 120:
                if click[0] == 1:
                    wm()
            click = pygame.mouse.get_pressed()
            screen.blit(kursor, mouse)
            pygame.display.update()


def first_round():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    kartX = screen.get_width()
    kartY = screen.get_height()
    pygame.display.set_caption("De Life")
    walk = [load_image('sperm1.png'), load_image('sperm2.png'),
            load_image('sperm3.png'), load_image('sperm4.png'),
            load_image('sperm5.png'), load_image('sperm6.png'),
            load_image('sperm7.png'), load_image('sperm8.png'), ]

    bg = pygame.transform.scale(load_image("bg4.png", 1), (kartX + 201, kartY))
    clock = pygame.time.Clock()
    x = 50
    y = 275
    xbg = kartX + 201
    xline = 21
    width = 100
    height = 50
    speed = 5

    animCount = 0
    run = True
    down = False
    while run:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and y < kartY - height - 5:
            y = y + speed
        if keys[pygame.K_SPACE] and xline >= kartX - 20:
            second_round()
        if keys[pygame.K_UP] and y > 5:
            y = y - speed
        if keys[pygame.K_LEFT] and x > 5:
            x = x - speed
        if keys[pygame.K_RIGHT] and x < kartX - width - 100:
            x = x + speed

        screen.blit(bg, (-(kartX + 201 - xbg), 0))
        screen.blit(bg, (xbg, 0))
        xbg = xbg - 1

        if xbg == 0:
            xbg = 701

        pygame.draw.line(screen, (0, 0, 0), (20, 5), (kartX - 20, 5), 15)
        pygame.draw.line(screen, (0, 255, 0), (20, 5), (xline, 5), 15)
        xline = xline + 3

        if xline >= kartX - 20:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("Жизнь зародилась!", 1, (100, 255, 100))

            text_x = kartX // 2 - text.get_width() // 2
            text_y = kartY // 2 - text.get_height() // 2
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))
            pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                                   text_w + 20, text_h + 20), 1)

        if animCount + 1 >= 40:
            animCount = 0

        screen.blit(walk[animCount // 5], (x, y))
        animCount = animCount + 1

        pygame.display.update()


def second_round():
    FPS = 30
    Clock = pygame.time.Clock()
    pygame.mixer.music.stop()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    size = window_width, window_height = screen.get_width(), screen.get_height()
    pygame.display.set_caption('De Life')  # #название игры нужно придумать и поменять это
    x, y = 3000, 3000
    baby1 = pygame.transform.scale(load_image('babyLine.png'), (x, y))
    baby2 = pygame.transform.scale(load_image('babyLeft.png'), (x, y))
    baby3 = pygame.transform.scale(load_image('babyRight.png'), (x, y))
    room = pygame.transform.scale(load_image('room.png', 1), size)
    screen.blit(room, (0, 0))
    y1 = 400

    yRect = 300
    pygame.draw.rect(screen, (255, 0, 0), (50, 20, 50, 300))
    pygame.draw.rect(screen, (0, 255, 0), (50, 120, 50, 50))
    pygame.draw.rect(screen, (0, 0, 0), (48, 18, 52, 302), 2)
    screen.blit(baby1, (600, 400))
    pygame.display.flip()
    pygame.draw.rect(screen, (250, 250, 250), (50, yRect, 49, 10))
    pygame.display.update()
    n = 1
    g = True
    vy = 150
    flag = True
    walk = None
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not flag:
                    third_round()
                if event.key == pygame.K_SPACE and flag:
                    vy += 10
                    if flag:
                        baby1 = pygame.transform.scale(load_image('babyLine.png'), (x, y))
                        baby2 = pygame.transform.scale(load_image('babyLeft.png'), (x, y))
                        baby3 = pygame.transform.scale(load_image('babyRight.png'), (x, y))
                        screen.blit(room, (0, 0))
                    if n == 1:
                        screen.blit(baby2, (600, y1))
                    elif n == 2:
                        screen.blit(baby3, (600, y1))
                    elif n == 3:
                        screen.blit(baby1, (600, y1))
                    n = (n + 1) % 4
                    x -= 20
                    y -= 20
                    y1 -= 20
                    if n == 0:
                        n = 1
                    if y1 == 40:
                        flag = False
                        walk = pygame.transform.scale(load_image('walk.png', 1), (600, 500))
                        screen.blit(walk, (window_width // 2 - 300, window_height // 2 - 250))
                        g = False
                if 120 > yRect or yRect > 170 and event.key == pygame.K_SPACE:
                    babysit = pygame.transform.scale(load_image('babySit.png'), (x, y))
                    screen.blit(room, (0, 0))
                    screen.blit(babysit, (600, y1 + 100))
                if event.key == pygame.K_ESCAPE:
                    my_file = open("save.txt", "w")
                    my_file.write('second_round()')
                    my_file.close()
                    pygame.quit()
                    sys.exit()
        if g:
            pygame.draw.rect(screen, (255, 0, 0), (50, 20, 50, 300))
            pygame.draw.rect(screen, (0, 255, 0), (50, 120, 50, 50))
            pygame.draw.rect(screen, (0, 0, 0), (48, 18, 52, 302), 2)
            if yRect >= 300:
                k = -1
            elif yRect <= 20:
                k = 1
            yRect += k * vy * Clock.tick() / 1000
            pygame.draw.rect(screen, (250, 250, 250), (50, int(yRect), 49, 10))
        pygame.display.update()


def third_round():
    FPS = 30
    Clock = pygame.time.Clock()
    clock = pygame.time.Clock()
    pygame.mixer.music.stop()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((100, 250, 100))
    size = window_width, window_height = screen.get_width(), screen.get_height()
    pygame.display.set_caption('De Life')
    x = window_width * 3
    y = window_height
    city = pygame.transform.scale(load_image('city.png', 1), (x, y))
    xMap = 0
    screen.blit(city, (xMap * 5, 0))
    t = False
    xBoy = 50
    yBoy = 280
    boy = pygame.transform.scale(load_image('run1.png'), (70, 100))
    screen.blit(boy, (xBoy, yBoy))
    h = 9
    w = 51
    x2 = xMap
    run = [load_image('run1.png'), load_image('run2.png'), load_image('run3.png'), load_image('run4.png'),
           load_image('run5.png'), load_image('run6.png')]
    jump = [load_image('jump_fall.png'), load_image('jump_up.png')]
    hit = load_image('hit.png')
    pygame.display.update()
    n = 0
    p = True
    v = -20
    h = False
    while True:
        if p:
            screen.blit(city, (xMap * 5, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    boy = pygame.transform.scale(jump[0], (70, 100))
                    x2 = abs(xMap)
                    t = True
                    screen.blit(boy, (xBoy, yBoy - 70))
                if event.key == pygame.K_p:
                    pause = pygame.transform.scale(load_image("pause.png", 1), (500, 500))
                    screen.blit(pause, (400, 40))
                    p = False
                if event.key == pygame.K_s and not p:
                    p = True
                if event.key == pygame.K_ESCAPE:
                    my_file = open("save.txt", "w")
                    my_file.write('third_round()')
                    my_file.close()
                    pygame.quit()
                    sys.exit()
        if p:
            xMap += v * Clock.tick() / 1000
            if t:
                boy = pygame.transform.scale(jump[0], (70, 100))
                screen.blit(boy, (xBoy, yBoy - 70))
            if not t and not h:
                clock.tick(10)
                n = (n + 1) % len(run)
                boy = pygame.transform.scale(run[n], (70, 100))
                screen.blit(boy, (xBoy, yBoy))
            if x2 - abs(xMap) <= -30 and t:
                boy = pygame.transform.scale(jump[1], (70, 100))
                screen.blit(boy, (xBoy, yBoy - 70))
                t = False
            if(-60 > xMap > -100 or -130 > xMap > -170 or
                    -255 > xMap > -280 or -340 > xMap > -370 or
                    -465 > xMap > - 495 or -620 > xMap > -650):
                if not t:
                    boy = pygame.transform.scale(hit, (70, 100))
                    h = False
                    screen.blit(boy, (xBoy, yBoy))
            if -700 > xMap > -750:
                final()
                break
        pygame.display.update()


def final():
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((100, 250, 100))
    size = window_width, window_height = screen.get_width(), screen.get_height()
    pygame.display.set_caption('De Life')
    end = load_image("end.png", 1)
    screen.blit(end, (0, 0))
    logo = pygame.transform.scale(load_image('logo.png'), (128, 128))
    screen.blit(logo, (1200, 600))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# options()
game_intro()
# second_round()
