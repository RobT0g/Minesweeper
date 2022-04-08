import pygame

def getPos():
    pos = pygame.mouse.get_pos()
    return [int((pos[0]-16)/32), int((pos[1]-16)/32)]