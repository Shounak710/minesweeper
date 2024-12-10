# from env import MinesweeperEnv
# from stable_baselines3 import PPO

# mode = "mid"
# test_env = MinesweeperEnv(mode=mode)

# model = PPO.load(f"minesweeper_ppo_multi_mode")

# obs = test_env.reset()
# done = False

# print("Starting Minesweeper game with trained model...")
# moves = 0

# while not done:
#   action, _states = model.predict(obs)
  
#   obs, reward, done, info = test_env.step(action)
#   moves += 1

#   test_env.render()
  
#   print(f"Moves: {moves}, Action: {action}, Reward: {reward}")
#   if done:
#     if reward > 0:
#       print("Model won the game!")
#     else:
#       print("Model lost the game.")

from env import MinesweeperEnv
from stable_baselines3 import PPO
import numpy as np

# Set mode to the desired difficulty level
mode = "hard"
test_env = MinesweeperEnv(mode=mode)

# Load the trained model
model = PPO.load(f"minesweeper_ppo_multi_mode")

# Reset the environment and get the initial observation
obs, _ = test_env.reset()
done = False

# Initialize move counter
moves = 0

print("Starting Minesweeper game with trained model...")

if obs.ndim == 1:  # If only one environment, it will be a 1D array
  obs = np.expand_dims(obs, axis=0)

while not done:
  # Predict the next action
  action, _states = model.predict(obs, deterministic=True)
  
  # Convert the action to (x, y) coordinates
  x, y = divmod(action, test_env.board.horlen)  # Use `test_env.board.horlen` for grid width
  
  # Take the action in the environment
  obs, reward, done, _, info = test_env.step((x, y))
  
  moves += 1
  print(f"Move {moves}: Action taken - ({x}, {y}) | Reward: {reward}")
  
  # Optionally render the game board (if applicable)
  test_env.render()

# Final results
print(f"Moves: {moves}, Action: {action}, Reward: {reward}")
if done:
  if reward > 0:
    print("Model won the game!")
  else:
    print("Model lost the game.")
