import pygame as pg
from pygame.locals import *
import random
from Image import Image
from Pos import Pos
from functions import get_egg
class Chunk:
    image:Image
    step_x:int
    step_y:int

    def __init__(self,
                 top_left:Pos,
                 chunk_width:int,
                 chunk_height:int,
                 island_width:int
                 ,island_height:int):

        self.top_left = top_left
        self.chunk_width = chunk_width
        self.chunk_height = chunk_height
        self.island_width = random.randint(island_width//3,island_width)
        self.island_height = random.randint(island_height//3,island_height)
        self.offset_x = (self.chunk_width - self.island_width) // 2
        self.offset_y = (self.chunk_height - self.island_height) // 2

        self.body:list = []

        self.surface = pg.surface.Surface([self.island_width*Chunk.step_x,
                                           self.island_height*Chunk.step_y])

        self.surface.fill([255,255,255])

        self.make_dirt_chunk(top_left,self.island_width,self.island_height)

        self.update_surface()

        self.debug_color = [130,130,170]
        self.debug_color_border = [80,80,100]


    def make_dirt_chunk(self,top_left:Pos,island_width:int,island_height:int):

        for i in range(island_width):
            for c in range(island_height):
                if i==0 or c==0 or c==island_height-1 or i==island_width-1:
                    sprite = random.choice(Chunk.image.dirt_list)
                else:
                    sprite = random.choice(Chunk.image.water_list)

                self.body.append((top_left.get_transformed_pos(1,i,c),sprite))



    def update_surface(self):
        for i in self.body:
            self.surface.blit(i[1].transformed,
                              i[0].get_transformed_list(Chunk.step_x,
                              - (self.top_left.x + 0) * Chunk.step_x,
                              - (self.top_left.y + 0) * Chunk.step_y))

    def render_debug(self,screen:pg.surface.Surface,camera_rel:Pos):
        pg.draw.rect(screen,self.debug_color,
                     [
                         self.top_left.x * Chunk.step_x + camera_rel.x,
                         self.top_left.y * Chunk.step_y + camera_rel.y,
                         self.chunk_width * Chunk.step_x,
                         self.chunk_height * Chunk.step_y
                     ])

        pg.draw.rect(screen, self.debug_color_border,
                     [
                         self.top_left.x * Chunk.step_x + camera_rel.x,
                         self.top_left.y * Chunk.step_y + camera_rel.y,
                         1 * Chunk.step_x,
                         self.chunk_height * Chunk.step_y
                     ])

        pg.draw.rect(screen, self.debug_color_border,
                     [
                         self.top_left.x * Chunk.step_x + camera_rel.x,
                         self.top_left.y * Chunk.step_y + camera_rel.y,
                         self.chunk_width * Chunk.step_x,
                         1 * Chunk.step_y
                     ])

        pg.draw.rect(screen, self.debug_color_border,
                     [
                         (self.top_left.x+self.chunk_width-1) * Chunk.step_x + camera_rel.x,
                         self.top_left.y * Chunk.step_y + camera_rel.y,
                         1 * Chunk.step_x,
                         self.chunk_height * Chunk.step_y
                     ])

        pg.draw.rect(screen, self.debug_color_border,
                     [
                         self.top_left.x * Chunk.step_x + camera_rel.x,
                         (self.top_left.y+self.chunk_height-1) * Chunk.step_y + camera_rel.y,
                         self.chunk_width * Chunk.step_x,
                         1 * Chunk.step_y
                     ])


    def render(self,screen:pg.surface.Surface,camera_rel:Pos):

        screen.blit(self.surface,
                    self.top_left.get_transformed_list(Chunk.step_x,
                                                       camera_rel.x + self.offset_x * self.step_x,
                                                       camera_rel.y + self.offset_y * self.step_y))



