import pygame
from game_settings import *
from map import *
from player import *

pygame.init()
player = Player()

def mapping(x,y):
    return (x//TILE)*TILE, (y//TILE)*TILE

def ray_cast(screen, player_pos, player_angle):
    x1, y1 = player_pos
    x2, y2 = mapping(x1, y1)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin = math.sin(cur_angle)
        cos = math.cos(cur_angle)
        x, dx = (x2 + TILE, 1) if cos >= 0 else (x2, -1)
        for i in range(0, WIDTH, TILE):
            vdepth = (x - x1) / cos
            y = y1 + vdepth * sin
            if mapping(x+dx,y) in p_map:
                break
            x += dx*TILE
        y, dy = (y2 + TILE, 1) if sin >= 0 else (y2, -1)
        for i in range(0, HEIGHT, TILE):
            hdepth = (y-y1) / sin
            x = x1 + hdepth * cos
            if mapping(x,y+dy) in p_map:
                break
            y += dy*TILE
        depth = vdepth if vdepth < hdepth else hdepth
        depth *= math.cos( player_angle - cur_angle)
        
        proj_height = PROJ_CO / depth
        
        c = 255/(1+depth*depth*0.000003)
        color = (c//2,c//2,c//2) if vdepth < hdepth else (c//3,c//3,c//3)
        pygame.draw.rect(screen, color,(ray * SCALE, CENTERY-proj_height // 3, SCALE,proj_height))
        cur_angle += DELTA_ANGLE


    
