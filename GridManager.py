from random import randint

class Grid:
    def __init__(self, num) -> None:
        self.grid = [[0 for i in range(15)] for j in range(20)]
        self.bombs = [[randint(0, 19), randint(0, 14)] for i in range(num)]
        for i in self.bombs:
            while i in self.bombs[:(self.bombs.index(i))]:
                i = [randint(0, 19), randint(0, 14)]
            self.grid[i[0]][i[1]] = -1
        self.numbers = [[0 for i in range(15)] for j in range(20)]
        for k1, v1 in enumerate(self.grid):
            for k2, v2 in enumerate(v1):
                amnt = [self.grid[k1+i][k2+j] if (k1+i) in range(len(self.grid)) and (k2+j) in range(len(v1)) else 0 for i in [-1, 0, 1] for j in [-1, 0, 1]]
                self.numbers[k1][k2] = amnt.count(-1)
        self.opened = [[0 for i in range(15)] for j in range(20)]

    def openTile(self, tile) -> None:
        try:
            self.opened[tile[0]][tile[1]] = 1
        except:
            pass
