#INSTRUCTIONS: W,S and Up and Down Arrow to move forward and backward. Left and right arrows to turn. A and D are for moving left and right perpendicular to your direction. Q is for map

#It still crashes when u go into a wall :P
import pygame as pygame
pygame.init()
from game_settings import *
from player import *
from map import *
import math
from raycast import ray_cast
from drawing import Drawing
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen)

map_on = False
running = True

def check_map():
    global map_on
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        map_on = not map_on
        

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    player.movement()
    drawing.background()
    drawing.world(player.pos,player.angle)
    check_map()
    if map_on == True:
        pygame.draw.circle(screen, BLUE, (int(player.x, int(player.y))), 6)
        pygame.draw.line(screen, BLUE, player.pos,(player.x + 50 * math.cos(player.angle), player.y + 50 * math.sin(player.angle)))

    
        for x,y in p_map:
            pygame.draw.rect(screen, WHITE, (x,y,TILE,TILE),2)
    drawing.fps(clock)

    
    pygame.display.flip()
    clock.tick(FPS)