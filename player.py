from game_settings import *
from map import *
import pygame,math


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
    @property
    def pos(self):
        return(self.x,self.y)
    def movement(self):
        sin = math.sin(self.angle)
        cos = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        for depth in range(1):
            x2 = self.x + 15 * cos
            y2 = self.y + 15 * sin
            if (x2 // TILE*TILE, y2 // TILE*TILE) not in p_map:
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    self.x += player_speed * cos 
                    self.y += player_speed * sin
       
        for depth in range(1):
            x2 = self.x - 15 * cos
            y2 = self.y - 15 * sin
            if (x2 // TILE*TILE, y2 // TILE*TILE) not in p_map:
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    self.x -= player_speed * cos
                    self.y -= player_speed * sin
        for depth in range(1):
            x2 = self.x + 15 * sin
            y2 = self.y - 15 * cos
            if (x2 // TILE*TILE, y2 // TILE*TILE) not in p_map:
                if keys[pygame.K_a]:
                    self.x += player_speed * sin
                    self.y -= player_speed * cos
        for depth in range(1):
            x2 = self.x - 15 * sin
            y2 = self.y + 15 * cos
            if (x2 // TILE*TILE, y2 // TILE*TILE) not in p_map:
                if keys[pygame.K_d]:
                    self.x -= player_speed * sin
                    self.y += player_speed * cos
        if keys[pygame.K_LEFT]:
            self.angle -= player_rotation
        if keys[pygame.K_RIGHT]:
            self.angle += player_rotation
      
