import pygame
import Controller
from GridManager import Grid

class Screen:
    def __init__(self, display) -> None:
        self.display = display
        self.board = pygame.image.load('Images/Frame.png')
        self.square = pygame.image.load('Images/Square.png')
        self.bomb = pygame.image.load('Images/Bomb.png')
        self.font = pygame.font.SysFont('Times New Roman', 32)
        self.numbers = [self.font.render(f'{i}', False, ((i*80)%255, (i*135)%255, (i*40)%255)) for i in range(1, 10)]
        self.grid = Grid(40)
    
    def update(self):
        if p := Controller.getPos():
            self.grid.openTile(p)

    def module(self, v):
        if v >= 0:
            return v
        return -v

    def setOnScreen(self):
        self.display.blit(self.board, (0, 0))
        for k, v in enumerate(self.grid.grid):
            for k1, v1 in enumerate(v):
                if self.grid.opened[k][k1] != 0:
                    self.display.blit(self.square, (self.getActualPos((k, k1))))
                    if v1 == -1:
                        self.display.blit(self.bomb, (self.getActualPos((k, k1))))
                    if self.grid.numbers[k][k1] != 0 and v1 != -1:
                        pos = self.getActualPos((k, k1))
                        self.display.blit(self.numbers[self.grid.numbers[k][k1]-1], (pos[0]+9, pos[1]-2))
        pygame.display.flip()
    
    def getActualPos(self, pos):
        return [pos[0]*32 + 16, pos[1]*32 + 16]
