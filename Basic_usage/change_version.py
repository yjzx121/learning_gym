import time
import gym


env = gym.make("PongNoFrameskip-v4")
obs = env.reset()
print(dir(env.unwrapped))
while True:
    action = env.action_space.sample()
    obs, reward, done, _ = env.step(action)
    env.render()
    if done:
        break
