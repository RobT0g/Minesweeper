import pygame
from pygame.locals import *
from ScreenManager import Screen

pygame.init()                                                       # inicialização

screen_width = 21*32                                                # largura da tela
screen_height = 16*32                                               # altura da tela

display = pygame.display.set_mode((screen_width, screen_height))     # tela definida
pygame.display.set_caption('MineSweeper')                           # legenda da tela
screen = Screen(display)
screen.setOnScreen()

running = True                      # Variável de looping
while running:                      # looping
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN and not screen.dead:
            screen.update()
            screen.setOnScreen()
        if pygame.key.get_pressed()[pygame.K_SPACE] and screen.dead:
            screen.restart()
            screen.update()
            screen.setOnScreen()
        if pygame.key.get_pressed()[pygame.K_ESCAPE] or e.type == QUIT:
            running = False