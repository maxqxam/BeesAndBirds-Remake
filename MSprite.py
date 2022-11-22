import pygame as pg
from pygame.locals import *
from time import time

import random
from Sprite import Sprite
from Pos import Pos
from time import time

class MSprite:
    def __init__(self,sprite_list:list,
                 should_shuffle:bool=False,
                 tick_speed_list:list[float]=[0.5]):

        self.last_epoch:float = time()
        self.tick_speed:float = random.choice(tick_speed_list)
        self.x_flipped:bool = False
        self.y_flipped:bool = False
        self.should_shuffle = should_shuffle
        self.image_index:int = 0
        self.sprite_list:list = sprite_list


    def do_flips(self):
        for i in self.sprite_list:
            i.x_flipped = self.x_flipped
            i.y_flipped = self.y_flipped
            i.do_flips()

    def tick(self):
        if self.should_shuffle:
            self.image_index = random.randint(0,len(self.sprite_list)-1)
            return

        self.image_index += 1
        if self.image_index>=len(self.sprite_list):
            self.image_index = 0

    def check_events(self):
        T2 = time()
        if self.last_epoch + self.tick_speed < T2:
            self.last_epoch = T2
            self.tick()


    def render(self,screen:pg.surface.Surface,top_left_pos:Pos):
        self.sprite_list[self.image_index].render(screen,top_left_pos)

