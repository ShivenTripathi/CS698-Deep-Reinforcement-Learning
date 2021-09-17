import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class gaussianBandit(gym.Env):
    def __init__(self, size=10):
      '''
      '''
      self.rewards = []
      for i in range(size):
        self.rewards.append(np.random.normal(0,1))
      self.action_space = spaces.Discrete(size)
      self.observation_space = spaces.Discrete(1)

    def step(self, action):
      '''
      '''
      reward = 0
      reward = np.random.normal(self.rewards[action],1)
      return action, reward, True, None