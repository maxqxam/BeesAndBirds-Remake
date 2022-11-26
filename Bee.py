import pygame as pg
from pygame.locals import *

from Sprite import Sprite
from Chunk import Chunk
from MSprite import MSprite
from Image import Image
from Pos import Pos
from Rect import Rect
import random

class Bee:
    image: Image
    step_x: int
    step_y: int
    on_sim_chunks: list

    def __init__(self,top_left_pos:Pos,top_left_pos_rel:Pos,
                 size_scale:float,speed:float):

        self.top_left_pos = top_left_pos
        self.top_left_pos_rel = top_left_pos_rel
        self.size_scale = size_scale
        self.width = 0
        self.height = 0
        self.update_sprite()
        self.speed = speed
        self.is_on_fire = False
        self.is_flipped = False
        self.is_moving = False
        self.if_moved = False
        self.msprite = MSprite(Bee.image.bee_list,tick_speed_list=[0.15])
        self.fire_msprite = MSprite(Bee.image.bee_fire_list,tick_speed_list=[0.15])
        self.is_ghost = True
        self.move_request_list:list[Pos] = []


    def update_size_scale(self,new_size_scale:float):
        self.size_scale = new_size_scale
        old_width,old_height = self.width,self.height

        self.update_sprite()

        x_diff = abs(self.width - old_width)
        y_diff = abs(self.height - old_height)

        print(self.move(Pos(100,100)))


    def transform_size_scale(self,mult:float=1,plus:float=0):

        old_size_scale = self.size_scale
        self.size_scale *= mult
        self.size_scale += plus
        old_width, old_height = self.width, self.height
        self.update_sprite()
        x_diff = abs(self.width - old_width)
        y_diff = abs(self.height - old_height)

        if old_size_scale > self.size_scale:
            transform_result = self.move(Pos(x_diff/2, y_diff/2),False)
        else:
            transform_result = self.move(Pos(-x_diff/2, -y_diff/2),False)

        if not transform_result:
            self.size_scale = old_size_scale
            self.update_sprite()

    def update_sprite(self):

        for i in Bee.image.bee_list + Bee.image.bee_fire_list:
            i.newScaleByWidth(Bee.step_x * self.size_scale)
            i.do_flips()
            self.width,self.height = i.width,i.height

    def move_request(self,rel:Pos):
        self.move_request_list.append(rel)


    def move(self,rel:Pos ,
             should_do_flip:bool = True,
             first_rel:Pos=None) -> bool:

        if first_rel is None: first_rel = Pos(rel.x,rel.y)
        limit = first_rel.get_transformed_pos(0.01)
        if abs(rel.x) < abs(limit.x) or abs(rel.y) < abs(limit.y): return False

        for i in Bee.on_sim_chunks:
            if self.is_ghost:
                break

            rects = i.get_blocking_objects()
            for i in rects:
                print(self.get_rect().get_transformed_pos(1,rel.x,rel.y),i)

                if self.get_rect().get_transformed_pos(1,rel.x,rel.y).collides_width_rect(i):
                    return self.move(rel.get_transformed_pos(0.9),should_do_flip,first_rel)


        self.top_left_pos_rel.combine(rel)
        print(self.top_left_pos,self.top_left_pos_rel)

        if should_do_flip:
            if rel.x > 0: self.is_flipped = False
            if rel.x < 0: self.is_flipped = True

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

        return True

    def check_events(self):

        if len(self.move_request_list)!=0:
            self.if_moved = self.move(self.move_request_list[0])
            self.move_request_list.pop(0)


        if self.is_flipped ^ self.msprite.x_flipped:
            self.msprite.x_flipped = self.is_flipped
            self.fire_msprite.x_flipped = self.is_flipped
            self.msprite.do_flips()
            self.fire_msprite.do_flips()

        sprite = self.msprite
        if self.is_on_fire: sprite = self.fire_msprite

        if self.is_moving: sprite.check_events()

    def render_debug(self,screen:pg.surface.Surface,camera:Pos):
        self.get_rect().render(screen,camera.get_tuple())

    def render(self,screen:pg.surface.Surface,camera:Pos):
        sprite = self.msprite
        if self.is_on_fire: sprite = self.fire_msprite

        sprite.render(screen,
                    self.top_left_pos.get_transformed_pos(Bee.step_x
                         , self.top_left_pos_rel.x + camera.x,
                          self.top_left_pos_rel.y + camera.y))


    def get_rect(self) -> Rect:
        return self.top_left_pos.get_transformed_pos(Bee.step_x
                                              , self.top_left_pos_rel.x ,
                                              self.top_left_pos_rel.y).get_rect(self.width,
                                                                                self.height)

