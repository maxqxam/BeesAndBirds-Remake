import pygame as pg
from pygame.locals import *
import random
from Image import Image
from Pos import Pos

class Chunk:
    image:Image
    step_x:int
    step_y:int

    def __init__(self,
                 top_left:Pos,
                 width:int,
                 height:int,
                 max_width:int
                 ,max_height:int):

        self.top_left = top_left
        self.width = width
        self.height = height
        self.max_width = max_width
        self.max_height = max_height
        self.offset_x = (self.width - self.max_width) // 2
        self.offset_y = (self.height - self.max_height) // 2
        self.body:list = []

        self.surface = pg.surface.Surface([max_width*Chunk.step_x,
                                           max_height*Chunk.step_y])

        for i in range(max_width):
            for c in range(max_height):
                self.body.append(
                    (Pos(i + top_left.x + self.offset_x
                        ,c + top_left.y + self.offset_y),
                        random.choice(Chunk.image.dirt_list))
                                 )

        self.update_surface()

        self.debug_color = [130,130,170]

    def update_surface(self):
        for i in self.body:
            self.surface.blit(i[1].transformed,
                              i[0].get_transformed_list(Chunk.step_x,
                              - (self.top_left.x + self.offset_x) * Chunk.step_x,
                              - (self.top_left.y + self.offset_y) * Chunk.step_y))

    def render_debug(self,screen:pg.surface.Surface,camera_rel:Pos):
        pg.draw.rect(screen,self.debug_color,
                     [
                         self.top_left.x * Chunk.step_x + camera_rel.x,
                         self.top_left.y * Chunk.step_y + camera_rel.y,
                         self.width * Chunk.step_x,
                         self.height * Chunk.step_y
                     ])


    def render(self,screen:pg.surface.Surface,camera_rel:Pos):

        screen.blit(self.surface,
                    self.top_left.get_transformed_list(Chunk.step_x,
                                                       camera_rel.x + self.offset_x * self.step_x,
                                                       camera_rel.y + self.offset_y * self.step_y))


