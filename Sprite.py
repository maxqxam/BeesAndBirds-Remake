import pygame as pg
from pygame.locals import *

from Pos import Pos
class Sprite:

    auto_width = False
    auto_height = False
    width = 0
    height = 0

    def __init__(self,path:str,width:float=-1,height:float=-1):
        self.raw = pg.image.load(path)
        self.transformed = self.raw
        self.x_flipped:bool = False
        self.y_flipped:bool = False
        self.should_scaleX:bool = True
        self.should_scaleY:bool = True
        self.width:float = width
        self.height:float = height

        if width==-1:
            self.should_scaleX = Sprite.auto_width
            self.width = Sprite.width

        if height==-1:
            self.should_scaleY = Sprite.auto_height
            self.height = Sprite.height

        if Sprite.auto_width:
            self.newScaleByWidth(self.width)
        elif Sprite.auto_height:
            self.newScaleByHeight(self.height)

    def do_flips(self):
        if self.should_scaleX:
            self.newScaleByWidth(self.width)
        elif self.should_scaleY:
            self.newScaleByHeight(self.height)

        self.transformed = pg.transform.flip(self.transformed,self.x_flipped,self.y_flipped)

    def newScaleByWidth(self, newWidth:int):
        scale = self.raw.get_width() / self.raw.get_height()
        newScale = [int(round(newWidth)), int(round(newWidth / scale)) - 1]
        self.transformed = pg.transform.scale(self.raw, newScale)
        self.width , self.height = self.transformed.get_size()

    def newScaleByHeight(self, newHeight:int):
        scale = self.raw.get_height() / self.raw.get_width()
        newScale = [int(round(newHeight) / scale) - 1, int(round(newHeight))]
        self.transformed = pg.transform.scale(self.raw, newScale)
        self.width , self.height = self.transformed.get_size()


    def render(self,screen:pg.surface.Surface,top_left_pos:Pos):
        screen.blit(self.transformed,top_left_pos.get_list())

