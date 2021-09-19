import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import matplotlib.pyplot as plt

class RME(gym.Env):

    def __init__(self, goal_reward=1, step_reward=-0.04, rows=3, cols=4, total_space = 12, hole_reward=-1, 
    goal_loc=3, hole_loc=7, wall_loc= 5,prob=0.8, seed=21):
      '''
      '''
      self.goal_reward = goal_reward
      self.step_reward = step_reward
      self.hole_reward = hole_reward

      self.goal_loc = goal_loc
      self.hole_loc = hole_loc
      self.wall_loc = wall_loc

      self.EMPTY = 0
      self.WALL = 1
      self.HOLE = 2
      self.GOAL = 3

      self.LEFT = 0
      self.RIGHT = 1
      self.DOWN = 2
      self.UP = 3

      self.rows = rows
      self.cols = cols
      self.total_space = total_space

      self.maze = np.zeros(self.total_space)
      self.maze[self.wall_loc]  = self.WALL
      self.maze[self.hole_loc]  = self.HOLE
      self.maze[self.goal_loc]  = self.GOAL
      self.maze = np.reshape(self.maze, (self.rows,self.cols))

      self.action_space = spaces.Discrete(4)
      self.observation_space = spaces.Discrete(self.total_space)

      self.prob = prob

      self.state = None
      self.trace = []

    def movement(self, move, initial=None):
      '''
      Checks if a move is at edge or not

      0 1 2 3
      4 5 6 7
      8 9 10 11
      
      0,0 0,1 0,2 0,3
      1,0 1,1 1,2 1,3
      2,0 2,1 2,2 2,3
      '''
      if initial is None:
        initial = self.state

      x = initial // self.cols
      y = initial % self.cols

      w_x = self.wall_loc // self.cols
      w_y = self.wall_loc % self.cols

      if move == self.LEFT and ( y == 0 or (y == w_y+1 and x == w_x) ):
        return initial
      if move == self.RIGHT and ( y == self.cols - 1 or (y == w_y-1 and x == w_x) ):
        return initial
      if move == self.UP and ( x == 0 or (x == w_x+1 and y == w_y) ):
        return initial
      if move == self.DOWN and ( x == self.rows - 1 or (x == w_x-1 and y == w_y) ):
        return initial

      if move == self.LEFT:
        y-=1
      if move == self.RIGHT:
        y+=1
      if move == self.DOWN:
        x+=1
      if move == self.UP:
        x-=1
      
      return x * self.cols + y      

    def step(self, action):
      '''
      '''
      reward = self.step_reward
      terminal = False
    
      # x = self.state // self.cols
      # y = self.state % self.cols

      if np.random.rand(1) > self.prob:
        if action == self.LEFT or action == self.RIGHT:
          action = 2 + np.random.randint(2)
        if action == self.UP or action == self.DOWN:
          action = np.random.randint(2)
      
      # print(self.movement(move=action, initial=self.state))
      self.state = self.movement(move=action, initial=self.state)
      self.trace.append(self.state)

      if self.state == self.goal_loc:
        terminal = True
        reward = self.goal_reward

      if self.state == self.hole_loc:
        terminal = True
        reward = self.hole_reward

      return self.state, reward, terminal, None

    def reset(self, start_loc=0):
      '''
      '''
      self.state = start_loc
      self.trace = [start_loc]
      pass

    def render(self):
      '''
      '''
      fig,ax = plt.subplots()
      drawMaze = np.copy(self.maze)

      for step in self.trace:
        drawMaze[step//self.cols, step%self.cols] = 4
        for i in range(self.rows):
          for j in range(self.cols):
            c = drawMaze[i,j]
            if c == self.GOAL:
              c = 'g'
            elif c == self.HOLE:
              c = 'h'
            elif c == self.WALL:
              c = 'w'
            elif c == 4:
              c = 'v'
            else:
              c = 'e'
            ax.text(j,i,str(c),va='center',ha='center')
        ax.matshow(drawMaze)

      plt.title('Maze Render')
      plt.show()