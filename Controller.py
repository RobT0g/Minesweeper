import pygame

def getPos():
    pos = pygame.mouse.get_pos()
    if pos[0]%32 in range(3, 29):
        return [int(pos[0]/32) + 1, int(pos[1]/32) + 1]