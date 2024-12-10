from board import Board

class Game():
  def __init__(self, mode='easy'):
    self.mode = mode
    self.board = Board(mode=mode)
    self.game_active = True
    self.won = False

    self.cell_status = {}
    self._set_cell_statuses()

    self.num_hidden = self.board.horlen * self.board.verlen

    self.display_grid()
    print(' ')

  def restart(self):
    print('setting up board')
    self.board = Board(mode=self.mode)
    self.game_active = True
    self.won = False

    print('cell status reached')
    self.cell_status = {}

    print('cell status setup')
    self._set_cell_statuses()
    print('status done')

    self.num_hidden = self.board.horlen * self.board.verlen

    print('displaying grid')
    self.display_grid()

  def play(self):
    while (self.num_hidden > self.board.num_mines) and self.game_active:
      x = int(input("row number of cell: ")) - 1
      y = int(input("col number of cell: ")) - 1
      
      if not ((0 <= x < self.board.horlen) and (0 <= y < self.board.verlen)):
        print("invalid cell position. Please enter again.")
        continue

      self.reveal(x, y)
    
    if self.game_won():
      self.game_active = False
      self.won = True

      print("Game won !")
      
  def reveal(self, x, y):
    if self.cell_status[(int(x), int(y))] == 'mine':
      self.game_active = False

      for pos in self.cell_status:
        if self.cell_status[pos] == 'mine':
          self.cell_status[pos] = 'open'

      self.display_grid()
      print(' ')

      print('You trod on a mine, and now the game is mine ! <:()')
  
    elif self.cell_status[(int(x), int(y))] == 'hidden':
      self.cell_status[(int(x), int(y))] == 'open'
      self.num_hidden -= 1

      if self.board.grid[x, y] == 0:
        self.handle_blank_case(x, y)

      self.display_grid()
      print(' ')

  def game_won(self):
    return (self.num_hidden == self.board.num_mines)

  def handle_blank_case(self, x, y):
    def in_grid(x, y):
      return (0 <= x < self.board.horlen) and (0 <= y < self.board.verlen)
    
    if not in_grid(x, y):
      return
    
    if self.board.grid[x][y] != 0:
      return

    for row_num in [x-1, x, x+1]:
      for col_num in [y-1, y, y+1]:
        if in_grid(row_num, col_num) and (self.cell_status[(row_num, col_num)] == 'hidden'):
          self.cell_status[(row_num, col_num)] = 'open'
          self.num_hidden -= 1
          
          self.handle_blank_case(row_num, col_num)

  def display_grid(self):
    for row_num, row in enumerate(self.board.grid):
      vals = []

      for col_num, col in enumerate(row):
        if self.cell_status[(row_num, col_num)] == 'open':
          vals.append(str(col))
        else:
          vals.append('*')
      
      print(' '.join(vals))

  def _set_cell_statuses(self):    
    for row_num, row in enumerate(self.board.grid):
      for col_num, col in enumerate(row):
        if col == Board.MINE_CHAR:
          self.cell_status[(row_num, col_num)] = 'mine'
        else:
          self.cell_status[(row_num, col_num)] = 'hidden'

# game = Game("hard")
# game.play()