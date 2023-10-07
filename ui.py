import pygame
from settings import *

class UI:
    def __init__(self):
        
        #General Setup
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        #Bar Setup
        self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)

        #Convert Weapon Dict
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)


    def show_bar(self,current,max_amout,bg_rect,color):
        #Draw Backgroud
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

        #Converting Stats to Pixel
        ratio = current / max_amout
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        
        #Draw Bar
        pygame.draw.rect(self.display_surface,color,current_rect)
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

    def show_exp(self,exp):
        self.x = self.display_surface.get_size()[0] - 20
        self.y = self.display_surface.get_size()[1] - 20
        text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
        text_rect = text_surf.get_rect(bottomright = (self.x,self.y))
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(15,15))
        pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(15,15),3)
        self.display_surface.blit(text_surf,text_rect)

    def selection_box(self,left,top,has_switched):
        bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
        else:  
            pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
        return bg_rect

    def weapon_overlay(self,weapon_index,has_switched):
        self.y = self.display_surface.get_size()[1] - (self.display_surface.get_size()[1] // 10)
        bg_rect = self.selection_box(10,self.y,has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(weapon_surf,weapon_rect)

    def display(self,player):
        self.show_bar(player.health,player.stats['health'],self.health_bar_rect,HEALTH_COLOR)
        self.show_bar(player.energy,player.stats['energy'],self.energy_bar_rect,ENERGY_COLOR)
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)
        #self.selection_box(90,self.display_surface.get_size()[1] - (self.display_surface.get_size()[1] // 10)) #Magic