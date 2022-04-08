import pygame
import Controller
from GridManager import Grid

class Screen:
    def __init__(self, display) -> None:
        self.display = display
        self.board = pygame.image.load('Images/Frame.png')
        self.square = pygame.image.load('Images/Square.png')
        self.unclick = pygame.image.load('Images/Unclickable.png')
        self.bomb = pygame.image.load('Images/Bomb.png')
        self.cross = pygame.image.load('Images/Death.png')
        self.font = pygame.font.SysFont('Times New Roman', 32)
        self.numbers = [self.font.render(f'{i}', False, ((i*80)%255, (i*135)%255, (i*40)%255)) for i in range(1, 10)]
        self.grid = Grid(40)
        self.rect = pygame.Surface((16*32,9*32), pygame.SRCALPHA)
        self.rect.fill((255,255,255,128))       
        self.dead = False
    
    def update(self):
        if p := Controller.getPos():
            if p[2] and self.grid.openTile(p) == 0:
                self.death(p)
                self.dead = True
            if not p[2]:
                self.grid.addUnclick(p)

    def death(self, p):
        self.grid.clearAll()
        self.setOnScreen()
        deadtxt1 = self.font.render(f'{"Game end!":^27}', False, (0, 0, 0))
        deadtxt2 = self.font.render(f'{"Press Space to restart":^27}', False, (0, 0, 0))
        txt = f'Score: {self.grid.getScore()*100}'
        deadtxt3 = self.font.render(f'{txt:^27}', False, (0, 0, 0))
        self.display.blit(self.rect, (80, 112))
        self.display.blit(deadtxt1, ((6*32), (5*32)+16))
        self.display.blit(deadtxt3, ((6*32)+16, (7*32)+16))
        self.display.blit(deadtxt2, ((6*32), (8*32)+16))
        self.display.blit(self.cross, self.getActualPos((p[0], p[1])))
        pygame.display.flip()

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
            for i in self.grid.unclickable:
                self.display.blit(self.unclick, (self.getActualPos((i[0], i[1]))))
            pygame.display.flip()
    
    def getActualPos(self, pos):
        return [pos[0]*32 + 16, pos[1]*32 + 16]
    
    def restart(self):
        self.grid = Grid(40)
        self.dead = False
