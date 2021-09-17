import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class bernoulliBandit(gym.Env):
    def __init__(self,alpha,beta):
      '''
      '''
      self.probRewarded = [alpha,beta]
      self.rewards = [1,1]
      self.action_space = spaces.Discrete(2)
      self.observation_space = spaces.Discrete(1)

    def step(self, action):
      '''
      '''
      reward = 0
      if np.random.binomial(1,self.probRewarded[action]) is 1:
        reward = 1
      return action, reward, True, None