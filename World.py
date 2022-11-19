import pygame as pg
from pygame.locals import *

from Image import Image
from Chunk import Chunk
from Pos import Pos
from Bee import Bee

class World:
    def __init__(self,
                 step_x:int,step_y:int,
                 screen_width:int,screen_height:int):

        self.camera_rel:Pos = Pos(0,0)

        self.grid_step_x = step_x
        self.grid_step_y = step_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = Image(self.grid_step_x , self.grid_step_y)

        self.top_left = Pos(0,0)
        self.chunk_width = 12
        self.chunk_height = 12
        self.island_width = 9
        self.island_height = 9

        screen_width_grid = screen_width//step_x
        screen_height_grid = screen_height//step_y

        self.camera_rel.x = abs(screen_width_grid-self.chunk_width)//2
        self.camera_rel.y = abs(screen_height_grid-self.chunk_height)//2
        self.camera_rel.transform(step_x)


        Chunk.image = self.image
        Chunk.step_x = step_x
        Chunk.step_y = step_y

        self.chunks = {}

        self.generate_chunk_group(self.top_left)

        self.last_chunk = Pos(0,0)

        Bee.image = self.image
        Bee.step_x = step_x
        Bee.step_y = step_y

        self.player = Bee(Pos(self.chunk_width//2,self.chunk_height//2),
                          Pos(0,0),1,step_x//5)
        self.camera_rel.x -= self.player.width // 2
        self.camera_rel.y -= self.player.width // 2

    def get_current_chunk(self):
        x,y = self.camera_rel.get_list()
        x = -x + self.screen_width//2
        y = -y + self.screen_height//2

        x //= self.grid_step_x
        y //= self.grid_step_y

        x //= self.chunk_width
        y //= self.chunk_height

        return Pos(x,y)

    def get_adjacent_chunks(self):
        chunk_pos = self.get_current_chunk()

        return [
            chunk_pos.get_tuple(),

            (chunk_pos.x+1,chunk_pos.y),
            (chunk_pos.x-1, chunk_pos.y),
            (chunk_pos.x, chunk_pos.y+1),
            (chunk_pos.x, chunk_pos.y-1),

            (chunk_pos.x+1, chunk_pos.y+1),
            (chunk_pos.x+1, chunk_pos.y-1),
            (chunk_pos.x-1, chunk_pos.y+1),
            (chunk_pos.x-1, chunk_pos.y-1),

        ]


    def generate_chunk(self,top_left_rel:Pos) -> bool:

        if top_left_rel.get_tuple() in self.chunks:
            return False

        self.chunks[top_left_rel.get_tuple()] = Chunk(
            top_left_rel.get_transformed_pos(self.chunk_width)
            , self.chunk_width, self.chunk_height,
            self.island_width, self.island_height)

        return True

    def generate_chunk_group(self,top_left_rel:Pos):
        self.generate_chunk(top_left_rel)

        self.generate_chunk(top_left_rel.get_transformed_pos(1, 1, 0))
        self.generate_chunk(top_left_rel.get_transformed_pos(1, -1, 0))
        self.generate_chunk(top_left_rel.get_transformed_pos(1, 0, 1))
        self.generate_chunk(top_left_rel.get_transformed_pos(1, 0, -1))

        self.generate_chunk(top_left_rel.get_transformed_pos(1, 1, -1))
        self.generate_chunk(top_left_rel.get_transformed_pos(1, 1, +1))
        self.generate_chunk(top_left_rel.get_transformed_pos(1, -1, -1))
        self.generate_chunk(top_left_rel.get_transformed_pos(1, -1, +1))

    def check_events(self):
        new_chunk = self.get_current_chunk()

        if self.last_chunk.get_tuple() != new_chunk.get_tuple():
            self.generate_chunk_group(new_chunk)

        adjacent_chunks = self.get_adjacent_chunks()

        for i in self.chunks:
            if i in adjacent_chunks:
                self.chunks[i].check_events()


        self.last_chunk = new_chunk

    def render(self,screen:pg.surface.Surface):

        adjacent_chunks = self.get_adjacent_chunks()

        c = 0
        for i in self.chunks:
            if i in adjacent_chunks:
                self.chunks[i].render(screen, self.camera_rel)
                c+=1

        self.player.render(screen,self.camera_rel)

        print("rendered chunks : ",c,"total chunks : ",len(self.chunks))


    def render_debug(self,screen:pg.surface.Surface):

        x_offset = self.camera_rel.x % self.grid_step_x
        y_offset = self.camera_rel.y % self.grid_step_y

        adjacent_chunks = self.get_adjacent_chunks()
        for i in self.chunks:
            if i in adjacent_chunks:
                self.chunks[i].render_debug(screen,self.camera_rel)

        for i in range(0,
                       self.screen_width // self.grid_step_x):
            pg.draw.line(screen,[0,0,0],[i*self.grid_step_x + x_offset,0],
                         [i*self.grid_step_x + x_offset,self.screen_height])

        for i in range(0,
                       self.screen_height // self.grid_step_y):
            pg.draw.line(screen,[0,0,0],[0,i*self.grid_step_y + y_offset],
                         [self.screen_width,i*self.grid_step_y + y_offset])


