import pygame as pg
from pygame.locals import *

from Image import Image
from Pos import Pos

class Bee:
    image: Image
    step_x: int
    step_y: int

    def __init__(self,top_left_pos:Pos,width:int,speed:float):
        self.top_left_pos = top_left_pos
        self.width = width
        self.speed = speed
        self.is_on_fire = False
        self.is_flipped = False
        self.image_index = 0

    def check_events(self):
        0

    def render(self,screen:pg.surface.Surface,camera:Pos):
        screen.blit(Bee.image.bee_list[self.image_index].transformed,
                    self.top_left_pos.get_transformed_list(Bee.step_x,camera.x,camera.y))

