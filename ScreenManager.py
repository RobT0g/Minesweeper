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
        self.deathbox = pygame.Rect(80, 112, 16*32, 9*32)
        self.dead = False
    
    def update(self):
        if p := Controller.getPos():
            if self.grid.openTile(p) == 0:
                self.death()
                self.dead = True

    def death(self):
        deadtxt1 = self.font.render(f'{"Game end!":^27}', False, (0, 0, 0))
        deadtxt2 = self.font.render(f'{"Press Space to restart":^27}', False, (0, 0, 0))
        txt = f'Score: {self.grid.opened.count(1)*100}'
        deadtxt3 = self.font.render(f'{txt:^27}', False, (0, 0, 0))
        pygame.draw.rect(self.display, (19, 196, 181), self.deathbox)
        self.display.blit(deadtxt1, (80, (5*32)+16))
        self.display.blit(deadtxt2, (80, (8*32)+16))
        self.display.blit(deadtxt3, (80, (7*32)+16))
        pygame.display.flip()

    def module(self, v):
        if v >= 0:
            return v
        return -v

    def setOnScreen(self):
        if not self.dead:
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
    
    def restart(self):
        self.grid = Grid(40)
        self.dead = False
