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

        self.top_left = Pos(0,0)
        self.chunk_width = 15
        self.chunk_height = 15
        self.island_width = 10
        self.island_height = 10

        Chunk.image = self.image
        Chunk.step_x = step_x
        Chunk.step_y = step_y

        self.chunks = {
            (0,0) :
            Chunk(self.top_left,self.chunk_width,self.chunk_height,
                             self.island_width,self.island_height)
        }

        self.last_chunk = Pos(0,0)

    def get_current_chunk(self):
        x,y = self.camera_rel.get_list()
        x = -x
        y = -y

        x //= self.grid_step_x
        y //= self.grid_step_y

        x //= self.chunk_width
        y //= self.chunk_height

        return Pos(x,y)


    def render(self,screen:pg.surface.Surface):
        0


    def render_debug(self,screen:pg.surface.Surface):


        new_chunk = self.get_current_chunk()

        if self.last_chunk.get_tuple()!=new_chunk.get_tuple():
            print(len(self.chunks))
            self.chunks[new_chunk.get_tuple()] = Chunk(
                                new_chunk.get_transformed_pos(self.chunk_width)
                                            ,self.chunk_width,self.chunk_height,
                                        self.island_width,self.island_height)

        self.last_chunk = new_chunk

        x_offset = self.camera_rel.x % self.grid_step_x
        y_offset = self.camera_rel.y % self.grid_step_y

        for i in self.chunks:
            self.chunks[i].render_debug(screen,self.camera_rel)
            self.chunks[i].render(screen,self.camera_rel)

        for i in range(0,
                       self.screen_width // self.grid_step_x):
            pg.draw.line(screen,[0,0,0],[i*self.grid_step_x + x_offset,0],
                         [i*self.grid_step_x + x_offset,self.screen_height])

        for i in range(0,
                       self.screen_height // self.grid_step_y):
            pg.draw.line(screen,[0,0,0],[0,i*self.grid_step_y + y_offset],
                         [self.screen_width,i*self.grid_step_y + y_offset])


