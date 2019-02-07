# -*- coding:utf-8 -*-
"""
author:Cao Shawn
想做一个python3和pygame实现的烟花，但不能删除过时的火花，没有重力，
烟花数量也最多36个好像，后面估计会改改吧，2019新年快乐
"""
import pygame
import sys
import math
import random

fire_color = [(255, 255, 255), (255, 0, 0), (64, 224, 205),
                   (252, 230, 202), (237, 145, 33), (255, 255, 0)]
tho = 36
ro = 30


class Fireworks(pygame.sprite.Sprite):
    def __init__(self, screen, theat, random_color):
        super().__init__()
        self.screen = screen
        self.theat = theat
        self.color = random_color
        self.rect = pygame.Rect(0, 0, 2, 2)
        self.xo, self.yo = pygame.mouse.get_pos()
        self.rect.centerx = float(self.xo)
        self.rect.y = float(self.yo)
        self.r = float(((self.rect.centerx-self.xo)**2+(self.rect.y-self.yo)**2)**(1/2))

    def update(self):
        """火焰爆炸"""
        self.move_x = math.cos(self.theat * math.pi / (tho*(1/2))) * 5.
        self.move_y = math.sin(self.theat * math.pi / (tho*(1/2))) * 5.
        self.rect.centerx += self.move_x
        self.rect.y += self.move_y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def check_events(screen, expend_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            add_fire(screen, expend_group)


def update_fire(expend_group):
    expend_group.update()
    for fir in expend_group.copy():
        if fir.r > ro:
            expend_group.remove(fir)


def update_screen(screen, expend_group):
    screen.fill((0, 0, 0))
    for expend_grou in expend_group.sprites():
        expend_grou.draw()
    pygame.display.flip()


def add_fire(screen, expend_group):
    random_color = random.choice(fire_color)
    for theat in range(tho):
        new_firework = Fireworks(screen, theat, random_color)
        expend_group.add(new_firework)


def run_game():
    """初始游戏"""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    expend_group = pygame.sprite.Group()
    clock = pygame.time.Clock()
    while True:
        check_events(screen, expend_group)
        update_fire(expend_group)
        update_screen(screen, expend_group)
        clock.tick(30)


run_game()
