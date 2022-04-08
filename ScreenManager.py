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
        self.numbers = [self.font.render(f'{i}', False, (100, 100, 50)) for i in range(1, 10)]
        self.grid = Grid(40)
    
    def update(self):
        if p := Controller.getPos():
            pass

    def setOnScreen(self):
        self.display.blit(self.board, (0, 0))
        for k, v in enumerate(self.grid.grid):
            for k1, v1 in enumerate(v):
                if v1 == -1:
                    self.display.blit(self.bomb, (self.getActualPos((k, k1))))
                if self.grid.numbers[k][k1] != 0 and v1 != -1:
                    self.display.blit(self.numbers[self.grid.numbers[k][k1]-1], self.getActualPos((k, k1)))
        pygame.display.flip()
    
    def getActualPos(self, pos):
        return [pos[0]*32 + 16, pos[1]*32 + 16]
