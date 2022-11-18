import pygame as pg
from pygame.locals import *

from Image import Image
from Pos import Pos

class Bee:
    image: Image
    step_x: int
    step_y: int

    def __init__(self,top_left_pos:Pos,top_left_pos_rel:Pos,
                 width_scale:float,speed:float):

        self.top_left_pos = top_left_pos
        self.top_left_pos_rel = top_left_pos_rel
        self.width_scale = width_scale
        self.width = Bee.step_x * self.width_scale
        self.speed = speed
        self.is_on_fire = False
        self.is_flipped = False
        self.image_index = 0


    def move(self,rel:Pos):
        self.top_left_pos_rel.combine(rel)
        print(self.top_left_pos,self.top_left_pos_rel)
        if self.top_left_pos_rel.x >= Bee.step_x:
            self.top_left_pos.x += 1
            self.top_left_pos_rel.x -= Bee.step_x

        if self.top_left_pos_rel.y >= Bee.step_y:
            self.top_left_pos.y += 1
            self.top_left_pos_rel.y -= Bee.step_y

        if self.top_left_pos_rel.x < 0:
            self.top_left_pos_rel.x = Bee.step_x - abs(self.top_left_pos_rel.x)
            self.top_left_pos.x -= 1

        if self.top_left_pos_rel.y < 0:
            self.top_left_pos_rel.y = Bee.step_x - abs(self.top_left_pos_rel.y)
            self.top_left_pos.y -= 1





    def check_events(self):
        0

    def render(self,screen:pg.surface.Surface,camera:Pos):
        screen.blit(Bee.image.bee_list[self.image_index].transformed,
                    self.top_left_pos.get_transformed_list(Bee.step_x
                                                           ,self.top_left_pos_rel.x+camera.x,
                                                           self.top_left_pos_rel.y+camera.y))

