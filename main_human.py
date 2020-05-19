from pygame import *
from pygame.locals import *
import numpy
import sys
from util.constants import *
from util.functions import *
from time import sleep

disp = display.set_mode((screen_width*2, screen_height), 0, 32)
#disp = display.set_mode((screen_width, screen_height), 0, 32)

def game():
    reward = 0
    end = False
    while not end:
        #? Draw everything
        #draw_everything(disp)
        sleep(screen_sleep)

        #? Close game
        for e in event.get():
            if e.type==QUIT:
                quit()
                sys.exit()
        
        #? Get keyboard input
        keys = key.get_pressed()
        if keys[K_UP]:
            character_position[1] -= character_jump_power
        elif keys[K_DOWN]:
            character_position[1] += character_jump_power
        if character_position[1]<0:
            character_position[1] = 0
        elif character_position[1] > screen_height-character_dimensions[1]-ground_height:
            character_position[1] = screen_height-character_dimensions[1]-ground_height

        #? Generate terrain
        generate_terrain()
        #? Calculate Reward
        reward += calculate_reward()

        #? Collision checker
        cutout = (surfarray.pixels2d(disp.subsurface((0,0, screen_width/agent_vision,56)).copy()))        
        cutout[cutout == 16777215] = 0
        cutout[cutout == 65280] = 1
        #cutout[cutout == 255] = 0
        #draw_subspace(disp, cutout, character_position)
        draw_everything(disp, character_position)

        end = collision_checker()
    return reward

while True:
    print("SCORE:", game())
    character_position = reset_env()