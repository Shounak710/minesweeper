from env import MinesweeperEnv

# from stable_baselines3 import PPO
# from stable_baselines3.common.env_util import make_vec_env

# mode = "hard"
# env = make_vec_env(lambda: MinesweeperEnv(mode=mode), n_envs=4)
# model = PPO("MlpPolicy", env, verbose=1)

# model.learn(total_timesteps=1000000)
# model.save(f"minesweeper_{mode}_ppo")

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.env_util import make_vec_env

modes = ['easy', 'mid', 'hard']

# Create vectorized environment with wrapped Minesweeper environments
env = DummyVecEnv([lambda mode=mode: MinesweeperEnv(mode) for mode in modes])

# Initialize PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=500000)

# Save the model
model.save("minesweeper_ppo_multi_mode")

