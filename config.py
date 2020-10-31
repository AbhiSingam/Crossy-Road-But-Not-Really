#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
pygame.init()

scr_wid = 1000
scr_hei = 820
X = 1000
Y = 820
font = pygame.font.Font('freesansbold.ttf', 32)

text_config_1 = font.render('Player 1 crashed into an obstacle', True,
                            (255, 255, 255), (0, 0, 0))
text_config_1_Rect = text_config_1.get_rect()
text_config_1_Rect.center = (X // 2, Y // 2)

text_config_2 = font.render('Player 2 crashed into an obstacle', True,
                            (255, 255, 255), (0, 0, 0))
text_config_2_Rect = text_config_1.get_rect()
text_config_2_Rect.center = (X // 2, Y // 2)

text_config_3 = font.render('Player 1', True, (255, 255, 255), (0, 0,
                                                                0))
text_config_3_Rect = text_config_1.get_rect()
text_config_3_Rect.center = (X // 2, Y // 2)

text_config_4 = font.render('Player 2', True, (255, 255, 255), (0, 0,
                                                                0))
text_config_4_Rect = text_config_1.get_rect()
text_config_4_Rect.center = (X // 2, Y // 2)

text_config_5 = font.render('Player 1 completed the level', True, (255,
                                                                   255, 255), (0, 0, 0))
text_config_5_Rect = text_config_1.get_rect()
text_config_5_Rect.center = (X // 2, Y // 2)

text_config_6 = font.render('Player 2 completed the level', True, (255,
                                                                   255, 255), (0, 0, 0))
text_config_6_Rect = text_config_1.get_rect()
text_config_6_Rect.center = (X // 2, Y // 2)