import pygame as pg
from pygame.locals import *

from Pos import Pos
class Sprite:

    auto_scaleX = False
    auto_scaleY = False
    scaleX = 0
    scaleY = 0

    def __init__(self,path:str,scaleX:float=-1,scaleY:float=-1):
        self.raw = pg.image.load(path)
        self.transformed = self.raw
        self.x_flipped:bool = False
        self.y_flipped:bool = False
        self.should_scaleX:bool = True
        self.should_scaleY:bool = True
        self.scaleX:float = scaleX
        self.scaleY:float = scaleY

        if scaleX==-1:
            self.should_scaleX = Sprite.auto_scaleX
            self.scaleX = Sprite.scaleX

        if scaleY==-1:
            self.should_scaleY = Sprite.auto_scaleY
            self.scaleY = Sprite.scaleY

        if Sprite.auto_scaleX:
            self.newScaleByWidth(self.scaleX)
        elif Sprite.auto_scaleY:
            self.newScaleByHeight(self.scaleY)

    def do_flips(self):
        if self.should_scaleX:
            self.newScaleByWidth(self.scaleX)
        elif self.should_scaleY:
            self.newScaleByHeight(self.scaleY)

        self.transformed = pg.transform.flip(self.transformed,self.x_flipped,self.y_flipped)

    def newScaleByWidth(self, newWidth:int):
        scale = self.raw.get_width() / self.raw.get_height()
        newScale = [int(round(newWidth)), int(round(newWidth / scale)) - 1]
        self.transformed = pg.transform.scale(self.raw, newScale)

    def newScaleByHeight(self, newHeight:int):
        scale = self.raw.get_height() / self.raw.get_width()
        newScale = [int(round(newHeight) / scale) - 1, int(round(newHeight))]
        self.transformed = pg.transform.scale(self.raw, newScale)

    def render(self,screen:pg.surface.Surface,top_left_pos:Pos):
        screen.blit(self.transformed,top_left_pos.get_list())

