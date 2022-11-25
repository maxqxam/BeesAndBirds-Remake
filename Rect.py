import pygame as pg
from pygame.locals import *


class Rect:
    def __init__(self,x:float,y:float,width:float,height:float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return "<rect({},{},{},{})>".format(self.x,self.y,self.width,self.height)

    def get_pygame_rect(self) -> pg.rect.Rect:
        return pg.rect.Rect(self.x,self.y,self.width,self.height)

    def get_list(self):
        return [self.x,self.y,self.width,self.height]

    def get_tuple(self):
        return self.x,self.y,self.width,self.height

    def transform(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        self.x*=mult
        self.y*=mult
        self.x+=sum_x
        self.y+=sum_y

        self.width *= mult
        self.height *= mult
        self.width += sum_x
        self.height += sum_y

        return self

    def transform_pos(self,mult:float=1,sum_x:float=0,sum_y:float=0):
        self.x*=mult
        self.y*=mult
        self.x+=sum_x
        self.y+=sum_y

        return self

    def get_transformed_rect(self,mult:float=1,x_rel:float=0,y_rel:float=0):
        return Rect(self.x * mult + x_rel,
                    self.y * mult + y_rel,
                    self.width * mult
                    ,self.height * mult)

    def set_size(self,width:float,height:float):
        self.width = width
        self.height = height
        return self

    def collides_width_rect(self,rect):
        return self.get_pygame_rect().colliderect(rect.get_pygame_rect())

    def render(self,screen:pg.surface.Surface,camera_rel:tuple[float,float]):
        pg.draw.rect(screen,[0,0,0],
                     self.transform_pos(1,camera_rel[0],camera_rel[1]).get_pygame_rect())



