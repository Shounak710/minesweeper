from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import random
from env import MinesweeperEnv

# Function to create Minesweeper environment with different modes
def make_minesweeper_env(mode):
    return lambda: MinesweeperEnv(mode=mode)

# List of modes to alternate between
modes = ['easy', 'medium', 'hard']

# Create a single environment using DummyVecEnv
env = DummyVecEnv([make_minesweeper_env(modes[0])])  # Start with the 'easy' mode

# Define the PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Number of timesteps you want to train for
total_timesteps = 500000

# Training loop
for step in range(total_timesteps):
    if step % 10000 == 0:  # Change mode every 10,000 steps (for example)
        mode = random.choice(modes)  # Randomly choose a new mode
        env = DummyVecEnv([make_minesweeper_env(mode)])  # Create a new environment for the chosen mode
        model.set_env(env)  # Switch the environment for the model
    
    # Continue training on the new environment (model automatically trains on the current env)
    model.learn(total_timesteps=1)

# Save the trained model
model.save("minesweeper_ppo_multi_mode")

# Optionally, load and test the trained model
model = PPO.load("minesweeper_ppo_multi_mode")
obs = env.reset()
done = False

while not done:
    action, _states = model.predict(obs)
    obs, reward, done, info = env.step(action)
    env.render()
    print(f"Reward: {reward}")
