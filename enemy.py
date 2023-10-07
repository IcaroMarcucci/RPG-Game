import pygame
from settings import *
from entity import *

class Enemy(Entity):
    def __init__(self,monster_name,pos,groups):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        #Graphics Setup
        self.import_graphics(monster_name)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)

    def import_graphics(self,name):
        pass