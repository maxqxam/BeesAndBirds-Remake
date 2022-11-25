import pygame as pg
from pygame.locals import *

from Sprite import Sprite
from MSprite import MSprite

class Image:

    def __init__(self,step_x:int,step_y:int):

        Sprite.auto_width = True
        Sprite.width = step_x + 1

        self.dirt0 = Sprite('./images/dirt0.png')
        self.dirt1 = Sprite('./images/dirt1.png')
        self.top_dirt0 = Sprite('./images/top_dirt0.png')
        self.top_dirt1 = Sprite('./images/top_dirt1.png')
        self.bottom_dirt0 = Sprite('./images/bottom_dirt0.png')
        self.bottom_dirt1 = Sprite('./images/bottom_dirt1.png')

        self.stone0 = Sprite('./images/stone0.png')
        self.stone1 = Sprite('./images/stone1.png')
        self.top_stone0 = Sprite('./images/top_stone0.png')
        self.top_stone1 = Sprite('./images/top_stone1.png')
        self.bottom_stone0 = Sprite('./images/bottom_stone0.png')
        self.bottom_stone1 = Sprite('./images/bottom_stone1.png')

        self.water0 = Sprite('./images/water0.png')
        self.water1 = Sprite('./images/water1.png')
        self.water2 = Sprite('./images/water2.png')
        self.water3 = Sprite('./images/water3.png')
        self.water4 = Sprite('./images/water4.png')
        self.water5 = Sprite('./images/water5.png')

        self.dirtStone0 = Sprite('./images/dirtStone0.png')
        self.dirtStone1 = Sprite('./images/dirtStone1.png')

        self.fire0 = Sprite('./images/fire0.png')
        self.fire1 = Sprite('./images/fire1.png')
        self.fire2 = Sprite('./images/fire2.png')
        self.fire3 = Sprite('./images/fire3.png')
        self.fire4 = Sprite('./images/fire4.png')
        self.fire5 = Sprite('./images/fire5.png')

        self.bee0 = Sprite('./images/bee0.png')
        self.bee1 = Sprite('./images/bee1.png')
        self.bee2 = Sprite('./images/bee2.png')
        self.bee3 = Sprite('./images/bee3.png')



        self.bee_list = [self.bee0,self.bee1]
        self.bee_fire_list = [self.bee2,self.bee3]

        self.dirt_list = [self.dirt0,self.dirt1]
        self.top_dirt_list = [self.top_dirt0,self.top_dirt1]
        self.bottom_dirt_list = [self.bottom_dirt0,self.bottom_dirt1]

        self.stone_list = [self.stone0,self.stone1]
        self.top_stone_list = [self.top_stone0,self.top_stone1]
        self.bottom_stone_list = [self.bottom_stone0,self.bottom_stone1]

        self.dirtStone_list=[self.dirtStone0,self.dirtStone1]
        self.water_list = [self.water0,self.water1,self.water2,
                           self.water3,self.water4,self.water5]



        Sprite.auto_width = False
        Sprite.auto_height = True
        Sprite.height = step_y

        self.flower0 = Sprite('./images/flower0.png')
        self.flower1 = Sprite('./images/flower1.png')


        self.flower_list = [self.flower0,self.flower1]

        self.fire_list = [self.fire0,self.fire1,self.fire2,
                          self.fire3,self.fire4,self.fire5]









