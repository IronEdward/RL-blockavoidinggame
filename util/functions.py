from pygame import *
from pygame.locals import *
from util.constants import *
import numpy as np
import sys

def draw_everything(disp, character_position):
    global character_rect, game_terrain_rect_list
    disp.fill(screen_color)
    character_rect = draw.rect(disp, character_color, (character_position[0], character_position[1], character_dimensions[0], character_dimensions[1]))
    draw.rect(disp, ground_color, (0, screen_height-ground_height, screen_width, ground_height))
    game_terrain_rect_list = []
    for index, terrain in enumerate(game_terrain):
        game_terrain[index][0] -= game_speed
        if game_terrain[index][0] < -game_terrain_dimensions[0]:
            game_terrain.remove(game_terrain[index])
        game_terrain_rect_list.append(draw.rect(disp, game_terrain_color, (terrain[0], (screen_height-ground_height-terrain[1])*terrain[3], game_terrain_dimensions[0], terrain[1])))
    display.update()

def draw_subspace(disp, cutout, character_position):
    global character_rect, game_terrain_rect_list
    disp.fill(screen_color)
    character_rect = draw.rect(disp, character_color, (character_position[0], character_position[1], character_dimensions[0], character_dimensions[1]))
    draw.rect(disp, ground_color, (0, screen_height-ground_height, screen_width, ground_height))
    game_terrain_rect_list = []
    for index, terrain in enumerate(game_terrain):
        game_terrain[index][0] -= game_speed
        if game_terrain[index][0] < -game_terrain_dimensions[0]:
            game_terrain.remove(game_terrain[index])
        game_terrain_rect_list.append(draw.rect(disp, game_terrain_color, (terrain[0], (screen_height-ground_height-terrain[1])*terrain[3], game_terrain_dimensions[0], terrain[1])))
    picture = surfarray.make_surface(cutout)
    disp.blit(picture, (100,0))
    display.update()

def generate_terrain():
    global game_terrain
    if np.random.randint(0, game_terrain_generate_probability) == 0:
        side = np.random.randint(0, 2)
        game_terrain.append([screen_width, game_terrain_dimensions[1], 0, side])
        #game_terrain.append([screen_width, np.random.randint(int(game_terrain_dimensions[1]/4), game_terrain_dimensions[1]), 0])
    buf_game_terrain = list(game_terrain)
    for index, terrain in enumerate(game_terrain[:-1]):
        if abs(terrain[0] - game_terrain[index+1][0]) < game_terrain_minimum_distance_to_each_other+game_terrain_dimensions[0]:
            buf_game_terrain.remove(game_terrain[index+1])
    game_terrain = buf_game_terrain

def collision_checker():
    global character_rect, game_terrain_rect_list
    for terrain_rect in game_terrain_rect_list:
        if character_rect.colliderect(terrain_rect):
            return True
    return False

def reset_env():
    global character_on_ground, game_terrain, character_position
    character_on_ground = True
    game_terrain = []
    return list(character_initial_position)

def calculate_reward():
    global game_terrain
    buf_game_terrain = game_terrain
    reward = 0
    for index, block in enumerate(game_terrain):
        if block[0]+game_terrain_dimensions[0] < character_position[0] and block[2] != 1:
            reward = 100
            buf_game_terrain[index][2] = 1
    game_terrain = buf_game_terrain
    return reward
    #print(reward)