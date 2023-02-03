import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Sprite Setup
        self.create_map()


    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for column_index,column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'x':
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
                if column == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)



    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        # offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
