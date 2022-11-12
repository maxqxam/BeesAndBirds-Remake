import pygame as pg
from pygame.locals import *

class Sprite:

    auto_scaleX = False
    auto_scaleY = False
    scaleX = 50
    scaleY = 50

    def __init__(self,path:str):
        self.raw = pg.image.load(path)
        self.transformed = self.raw
        if Sprite.auto_scaleX:
            self.newScaleByWidth(self.scaleX)
        elif Sprite.auto_scaleY:
            self.newScaleByHeight(self.scaleY)

    def newScaleByWidth(self, newWidth:int):
        scale = self.raw.get_width() / self.raw.get_height()
        newScale = [int(round(newWidth)), int(round(newWidth / scale)) - 1]
        self.transformed = pg.transform.scale(self.raw, newScale)

    def newScaleByHeight(self, newHeight:int):
        scale = self.raw.get_height() / self.raw.get_width()
        newScale = [int(round(newHeight) / scale) - 1, int(round(newHeight))]
        self.transformed = pg.transform.scale(self.raw, newScale)
