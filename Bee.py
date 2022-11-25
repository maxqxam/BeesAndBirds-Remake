import pygame as pg
from pygame.locals import *

from Sprite import Sprite
from Chunk import Chunk
from MSprite import MSprite
from Image import Image
from Pos import Pos
from Rect import Rect

class Bee:
    image: Image
    step_x: int
    step_y: int
    on_sim_chunks: list

    def __init__(self,top_left_pos:Pos,top_left_pos_rel:Pos,
                 width_scale:float,speed:float):

        self.top_left_pos = top_left_pos
        self.top_left_pos_rel = top_left_pos_rel
        self.width_scale = width_scale
        self.width = Bee.step_x * self.width_scale
        self.speed = speed
        self.is_on_fire = False
        self.is_flipped = False
        self.is_moving = False
        self.msprite = MSprite(Bee.image.bee_list,tick_speed_list=[0.15])
        self.fire_msprite = MSprite(Bee.image.bee_fire_list,tick_speed_list=[0.15])
        self.is_ghost = True
        self.move_request_list:list[Pos] = []



    def move_request(self,rel:Pos):
        self.move_request_list.append(rel)


    def move(self,rel:Pos) -> bool:

        for i in Bee.on_sim_chunks:
            if self.is_ghost:
                break

            rects = i.get_blocking_objects()
            for i in rects:
                print(self.get_rect(),i)

                if self.get_rect().collides_width_rect(i):
                    return False


        self.top_left_pos_rel.combine(rel)
        print(self.top_left_pos,self.top_left_pos_rel)

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
            self.move(self.move_request_list[0])
            self.move_request_list.pop(0)


        if self.is_flipped ^ self.msprite.x_flipped:
            self.msprite.x_flipped = self.is_flipped
            self.fire_msprite.x_flipped = self.is_flipped
            self.msprite.do_flips()
            self.fire_msprite.do_flips()

        sprite = self.msprite
        if self.is_on_fire: sprite = self.fire_msprite

        if self.is_moving: sprite.check_events()


    def render(self,screen:pg.surface.Surface,camera:Pos):
        for i in Bee.on_sim_chunks:
            rects = i.get_blocking_objects()

            for c in rects:
                c.render(screen,camera.get_tuple())

        sprite = self.msprite
        if self.is_on_fire: sprite = self.fire_msprite

        sprite.render(screen,
                    self.top_left_pos.get_transformed_pos(Bee.step_x
                         , self.top_left_pos_rel.x + camera.x,
                          self.top_left_pos_rel.y + camera.y))


    def get_rect(self) -> Rect:
        return self.top_left_pos.get_transformed_pos(Bee.step_x
                                              , self.top_left_pos_rel.x ,
                                              self.top_left_pos_rel.y).get_rect(Bee.step_x,
                                                                                Bee.step_y)

