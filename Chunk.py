import pygame as pg
from pygame.locals import *
import random
from time import time
from MSprite import MSprite
from Sprite import Sprite
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

        # self.surface.set_colorkey([0,0,0])

        func = random.choice([self.make_stone_pool,self.make_dirt_chunk])

        func(top_left,self.island_width,self.island_height)

        self.last_epoch:float = time()
        self.tick_speed:float = 0.05


        self.update_surface()

        self.debug_color = [130,130,170]
        self.debug_color_border = [80,80,100]


    def make_stone_pool(self,top_left:Pos,island_width:int,island_height:int):

        for i in range(island_width):
            for c in range(1,island_height):
                sprite = Chunk.image.water_msprite

                if i==0 or i==island_width-1 or c==island_height-1:
                    sprite = random.choice(Chunk.image.stone_list)
                    if c==1:
                        sprite = random.choice(Chunk.image.top_stone_list)

                self.body.append((top_left.get_transformed_pos(1,i,c),sprite))

        for i in [0,island_width-1]:
            egg = get_egg(4,1)
            if egg:
                sprite = Chunk.image.fire0
                self.body.append((top_left.get_transformed_pos(1,i,0),sprite))




    def make_dirt_chunk(self,top_left:Pos,island_width:int,island_height:int):

        for i in range(island_width):
            for c in range(1,island_height):
                sprite = random.choice(Chunk.image.dirt_list)
                if c==1:
                    sprite = random.choice(Chunk.image.top_dirt_list)
                    egg = 1
                else:
                    egg = get_egg(c,island_height-c)

                if egg == 0 or c == island_height-1:
                    sprite = random.choice(Chunk.image.bottom_dirt_list)


                self.body.append((top_left.get_transformed_pos(1,i,c),sprite))
                if egg == 0: break

        for i in range(island_width):
            egg = get_egg(island_width-i,i)
            if egg:
                sprite = random.choice(Chunk.image.flower_list)

                self.body.append((top_left.get_transformed_pos(1, i, 0), sprite))


    def check_events(self):

        for i in self.body:
            if type(i[1])==MSprite:
                i[1].check_events()

        T2 = time()
        if self.last_epoch + self.tick_speed < T2:
            self.last_epoch = T2
            self.update()




    def update(self):
        self.update_surface()


    def update_surface(self):
        for i in self.body:

            i[1].render(self.surface,
                        i[0].get_transformed_pos(Chunk.step_x,
                                                 - (self.top_left.x + 0) * Chunk.step_x,
                                                 - (self.top_left.y + 0) * Chunk.step_y)
                        )


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



