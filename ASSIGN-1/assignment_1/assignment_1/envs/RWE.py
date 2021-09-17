import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class RWE(gym.Env):

    def __init__(self, n_states=7, prob=0.5):
      '''
      '''
      self.n_states = n_states
      self.state = self.n_states//2
      self.action_space = spaces.Discrete(2)
      self.prob_correct = prob

    def step(self, action):
      '''
      '''
      reward = 0
      terminal = False

      if action == 0:
        if np.random.rand(1) < self.prob_correct:
          self.state -= 1
        else:
          self.state += 1
      else:
        if np.random.rand(1) < self.prob_correct:
          self.state += 1
        else:
          self.state -= 1

      if self.state == self.n_states-1 or self.state == 0:
        terminal = True

      if self.state == self.n_states-1:
        reward = 1

      return self.state, reward, terminal, None

    def reset(self):
      '''
      '''
      self.state = self.n_states//2