from random import randint

class Grid:
    def __init__(self) -> None:
        self.grid = [[-1 for i in range(15)] for j in range(20)]
        self.bombs = [[randint(0, 19), randint(0, 14)] for i in range(25)]
        for i in self.bombs:
            while self.grid[i[0]][i[1]] != 0:
                i = [randint(0, 19), randint(0, 14)]
            self.grid[i[0]][i[1]] = -2