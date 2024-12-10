from env import MinesweeperEnv
from stable_baselines3 import PPO

mode = "mid"
test_env = MinesweeperEnv(mode=mode)

model = PPO.load(f"minesweeper_{mode}_ppo")

obs = test_env.reset()
done = False

print("Starting Minesweeper game with trained model...")
moves = 0

while not done:
  action, _states = model.predict(obs)
  
  obs, reward, done, info = test_env.step(action)
  moves += 1

  test_env.render()
  
  print(f"Moves: {moves}, Action: {action}, Reward: {reward}")
  if done:
    if reward > 0:
      print("Model won the game!")
    else:
      print("Model lost the game.")