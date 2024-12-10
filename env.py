import gymnasium as gym
from gymnasium import spaces
import numpy as np
from game import Game
import random

class MinesweeperEnv(gym.Env):
  def __init__(self, mode='easy'):
    super().__init__()
    self.game = Game(mode=mode)
    self.board = self.game.board
    
    # self.grid_size = self.board.horlen * self.board.verlen
    self.max_grid_size = 15 * 14 # for hard mode
    self.done = False
    self.random_seed = None

    self.action_space = spaces.Discrete(self.max_grid_size)
    self.observation_space = spaces.Box(
      low=-1, high=8, shape=(self.max_grid_size,), dtype=int
    )

  def seed(self, seed=None):
    self.random_seed = seed
    
    random.seed(seed)
    np.random.seed(seed)  # If you're using numpy
    
    return [seed]
  
  def reset(self, seed=None, options=None):
    print(f'resetting {random.randint(1000, 110000000)}...')

    self.game.restart()
    self.done = False

    return self.get_observation(), {}

  def step(self, action):
    print('Taking a step with action: {action}')
    if self.done:
      return self.get_observation(), 0, self.done, False, {}

    x, y = divmod(action[0], self.board.horlen)

    if x >= self.board.horlen or y >= self.board.verlen:
      print(f"Invalid action: x={x}, y={y}")
      return self.get_observation(), -1, self.done, False, {}
    
    if self.game.cell_status[(int(x), int(y))] == 'open':
      return self.get_observation(), 0, self.done, False, {}

    self.game.reveal(x, y)

    if not self.game.game_active:
      self.done = True
      
      if self.game.won:
        reward = 10
      else:
        reward = -10  # Losing penalty
    else:
      reward = 1

    return self.get_observation(), reward, self.done, False, {}

  def get_observation(self):
    flat_grid = np.array(self.game.board.grid).flatten()
    padded_grid = np.pad(flat_grid, (0, self.max_grid_size - len(flat_grid)), constant_values=-1)

    return padded_grid
    # return np.array(self.game.board.grid).flatten()

  def render(self, mode="human"):
    self.game.display_grid()

    # for row in self.game.board.grid:
    #   print(" ".join(str(cell) if cell != -1 else "□" for cell in row))
    # print()