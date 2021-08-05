import pygame
from game_settings import *
from raycast import *
class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 36, bold = True)
    def background(self):
        pygame.draw.rect(self.screen, LIGHTBLUE, (0,0,WIDTH, CENTERY))
        pygame.draw.rect(self.screen, (150,150,150), (0,CENTERY,WIDTH,CENTERY))
    def world(self, player_pos, player_angle):
        ray_cast(self.screen, player_pos,player_angle)
    def fps(self, clock):
        display_fps = 'FPS: ' + str(int(clock.get_fps()))
        render = self.font.render(display_fps,0, BLUE)
        self.screen.blit(render, FPS_POS)
    