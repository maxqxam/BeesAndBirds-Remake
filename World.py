import pygame as pg
from pygame.locals import *

from Image import Image
from Chunk import Chunk
from Pos import Pos

class World:
    def __init__(self,
                 step_x:int,step_y:int,
                 screen_width:int,screen_height:int):

        self.camera_rel:Pos = Pos(0,0)

        self.grid_step_x = step_x
        self.grid_step_y = step_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = Image(self.grid_step_x)
        Chunk.image = self.image
        Chunk.step_x = step_x
        Chunk.step_y = step_y
        self.chunks = [Chunk(Pos(5,5),16,16,9,8)]


    def render(self,screen:pg.surface.Surface):
        0




    def render_debug(self,screen:pg.surface.Surface):

        x_offset = self.camera_rel.x % self.grid_step_x
        y_offset = self.camera_rel.y % self.grid_step_y


        for i in self.chunks:
            i.render_debug(screen,self.camera_rel)
            i.render(screen,self.camera_rel)

        for i in range(0,
                       self.screen_width // self.grid_step_x):
            pg.draw.line(screen,[0,0,0],[i*self.grid_step_x + x_offset,0],
                         [i*self.grid_step_x + x_offset,self.screen_height])

        for i in range(0,
                       self.screen_height // self.grid_step_y):
            pg.draw.line(screen,[0,0,0],[0,i*self.grid_step_y + y_offset],
                         [self.screen_width,i*self.grid_step_y + y_offset])


