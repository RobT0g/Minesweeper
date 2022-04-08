import pygame
import Controller
from GridManager import Grid

class Screen:
    def __init__(self, display) -> None:
        self.display = display
        self.board = pygame.image.load('Images/Frame.png')
        self.square = pygame.image.load('Images/Square.png')
        self.bomb = pygame.image.load('Images/Bomb.png')
        self.font = pygame.font.SysFont('Courier New', 32)
        self.numbers = self.font.render('1', False, (100, 100, 100))
        self.grid = Grid()
    
    def update(self):
        if p := Controller.getPos():
            pass

    def setOnScreen(self):
        self.display.blit(self.board, (0, 0))
        for k, v in enumerate(self.grid.grid):
            for k1, v1 in enumerate(v):
                if v1 == -2:
                    self.display.blit(self.bomb, (self.getActualPos((k, k1))))
        self.display.blit(self.numbers, self.getActualPos((3, 4)))
        pygame.display.flip()
    
    def getActualPos(self, pos):
        return [pos[0]*32 + 16, pos[1]*32 + 16]
