import pygame
from settings import *
from tile import *
from player import *
from debug import Debug

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        #Sprite Group
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        #Update and draw
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        Debug(self.player.direction)