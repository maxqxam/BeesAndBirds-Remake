import pygame as pg
from pygame.locals import *

from World import World

class Game:
    def __init__(self,screen:pg.surface.Surface):
        self.screen = screen
        self.is_over = False
        self.X = 1000
        self.Y = 750
        self.smask = pg.surface.Surface([self.X,self.Y])
        self.world = World(50,50,self.X,self.Y)
        self.held_keys = []



    def get_events(self):
        for i in pg.event.get():
            if i.type==QUIT or i.type==KEYUP and i.key==K_ESCAPE:
                self.is_over = True

            elif i.type==KEYDOWN:
                if i.key not in self.held_keys:
                    self.held_keys.append(i.key)

            elif i.type==KEYUP:
                if i.key in self.held_keys:

                    self.held_keys.remove(i.key)

    def check_events(self):

        self.world.check_events()

        step = 10
        if K_RIGHT in self.held_keys:
            self.world.camera_rel.x-=step

        elif K_LEFT in self.held_keys:
            self.world.camera_rel.x+=step

        if K_UP in self.held_keys:
            self.world.camera_rel.y+=step

        elif K_DOWN in self.held_keys:
            self.world.camera_rel.y-=step


    def update_and_render(self):

        self.smask.fill([180,220,255])

        self.world.render_debug(self.smask)
        self.world.render(self.smask)

        scaled_smask = pg.transform.scale(self.smask,[self.screen.get_width(),
                                                      self.screen.get_height()])

        self.screen.blit(scaled_smask,[0,0])
        pg.display.update()


    def run(self):
        self.get_events()
        self.check_events()
        self.update_and_render()



