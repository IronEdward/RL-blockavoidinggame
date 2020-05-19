import gym
from gym import spaces
from util.constants import *
from util.functions import *
from pygame import *
from pygame.locals import *
import numpy as np

def next_observation(disp, width, height):
	next_state = (surfarray.pixels2d(disp.subsurface((0,0,width,height)).copy()))        
	next_state[next_state == 16777215] = 0
	next_state[next_state == 65280] = 1
	return next_state

class BlockAvoid(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		super(BlockAvoid, self).__init__()
		self.disp = display.set_mode((screen_width, screen_height), 0, 32)
		self.N_DISCRETE_ACTIONS = 3
		self.WIDTH = int(screen_width/agent_vision)
		self.HEIGHT = int(screen_height - ground_height)
		self.action_space = spaces.Discrete(self.N_DISCRETE_ACTIONS)
		self.observation_space = spaces.Box(low=0, high=1, shape=(self.WIDTH, self.HEIGHT), dtype=np.uint8)

	def step(self, action):
		global character_position
		if action == 1:
			character_position[1] -= character_jump_power
		elif action == 2:
			character_position[1] += character_jump_power

		if character_position[1]<0:
			character_position[1] = 0
		elif character_position[1] > screen_height-character_dimensions[1]-ground_height:
			character_position[1] = screen_height-character_dimensions[1]-ground_height
		generate_terrain()
		reward = calculate_reward()
		next_state = next_observation(self.disp, self.WIDTH, self.HEIGHT)
		draw_everything(self.disp, character_position)
		done = collision_checker()
		return next_state, reward, done, {}		
    	  
	def reset(self):
		global character_position
		character_position = reset_env()
		return next_observation(self.disp, self.WIDTH, self.HEIGHT)