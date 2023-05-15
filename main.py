import gymnasium
import os

#pip install gymnasium[atari, accept-rom-licesnse]
# https://github.com/mgbellemare/Arcade-Learning-Environment#rom-management

#pip3 install "autorom[accept-rom-license]"
#env = gym.make("LunarLander-v2", render_mode="human")

#pip install gymnasium[atari]
#pip install gymnasium[accept-rom-license]

env = gymnasium.make("ALE/Asteroids-v5", render_mode="human", obs_type="grayscale")
observation, info = env.reset(seed=42)
#for _ in range(1000):
while True:
  action = env.action_space.sample()  # this is where you would insert your policy
  observation, reward, terminated, truncated, info = env.step(action)
  print("action: ", action)

  if terminated or truncated:
    observation, info = env.reset()
env.close()