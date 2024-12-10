import random
import numpy as np

class Board:
  MINE_CHAR = -1

  def __init__(self, mode='easy'):
    self.mode = mode

    self.reset_board()

  def reset_board(self):
    (self.horlen, self.verlen), self.num_mines = self._get_grid_counts()
    self.grid = np.zeros((self.horlen, self.verlen), dtype=int)

    self._plant_mines()

  def _get_grid_counts(self):
    if self.mode == 'easy':
      grid_dim = (6, 6)
      mine_proportion = 0.1
    elif self.mode == 'mid':
      grid_dim = (10, 8)
      mine_proportion = 0.14
    elif self.mode == 'hard':
      grid_dim = (15, 14)
      mine_proportion = 0.2
    else:
      dim = random.choice([6, 8, 10, 11, 13, 15, 18])
      grid_dim = (dim, dim)
      mine_proportion = random.uniform(0.1, 0.2)

    return grid_dim, int(mine_proportion * grid_dim[0] * grid_dim[1])

  def _plant_mines(self):
    count = 0
    
    while count < self.num_mines:
      x = random.randint(0, self.horlen-1)
      y = random.randint(0, self.verlen-1)

      if self.grid[x][y] == 0:
        self.grid[x][y] = Board.MINE_CHAR
        count += 1

        self._update_adjacent_counts(x, y)

  def _update_adjacent_counts(self, x, y):
    for x_c in [x-1, x, x+1]:
      for y_c in [y-1, y, y+1]:
        if (0 <= x_c <= self.horlen-1) and (0 <= y_c <= self.verlen-1) and (self.grid[x_c][y_c] != Board.MINE_CHAR):
          self.grid[x_c][y_c] += 1
