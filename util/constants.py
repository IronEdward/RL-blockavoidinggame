"""CONSTANTS"""

#* Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#* Screen dimensions
screen_width = 100
screen_height = 60
screen_color = WHITE
screen_sleep = 0.01

#* Ground
ground_height = 10
ground_color = BLACK


#* Character
character_dimensions = (5, 5)
character_initial_position = (10, screen_height - character_dimensions[1] - ground_height)
character_position = list(character_initial_position)
character_color = BLUE
character_on_ground = True
character_gravity = 0
character_jump_power = 5
character_velocity = 0
character_rect = None
character_moves = [0, ]

#* Screen(Gameplay)
game_speed = 1
game_terrain = []
game_terrain_dimensions = (3, (screen_height-ground_height-character_dimensions[1])/2)
#game_terrain_dimensions = (3, screen_height-ground_height-character_dimensions[1])
game_terrain_color = GREEN
game_terrain_generate_probability = 50
game_terrain_minimum_distance_to_each_other = 50
game_terrain_rect_list = []

#* RL Parameters
agent_vision = 1
end = False