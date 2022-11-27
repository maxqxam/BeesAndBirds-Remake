import pygame as pg
from pygame.locals import *

from World import World
from Pos import Pos
from Bee import Bee
class Game:
    def __init__(self,screen:pg.surface.Surface):
        self.screen = screen
        self.is_over = False
        self.X = 1000
        self.Y = 750
        self.smask = pg.surface.Surface([self.X,self.Y])
        self.world = World(50,50,self.X,self.Y)
        self.held_keys = []
        self.should_render_debug = False


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

                if i.key==K_F1:
                    self.should_render_debug = not self.should_render_debug

    def check_events(self):

        step = 10
        move_rel:Pos = Pos(0,0)

        self.world.player.is_ghost = K_LSHIFT in self.held_keys

        if K_1 in self.held_keys and self.world.player.size_scale > 0.11:
            self.world.player.transform_size_scale(plus=-0.1)

        if K_2 in self.held_keys and self.world.player.size_scale < 10:
            self.world.player.transform_size_scale(plus=0.1)


        if K_RIGHT in self.held_keys:move_rel.x = step
        elif K_LEFT in self.held_keys:move_rel.x = -step
        if K_UP in self.held_keys:move_rel.y = -step
        elif K_DOWN in self.held_keys:move_rel.y = step

        if move_rel.x!=0 or move_rel.y!=0:
            self.world.player.is_moving = True
            self.world.player.move_request(move_rel)
        else:
            self.world.player.is_moving = False

        last_player_pos = self.world.player.get_pos()
        self.world.check_events()
        if self.world.player.if_moved:
            self.world.camera_on_hold_move.combine(last_player_pos.get_diff(self.world.player.get_pos()))



    def update_and_render(self):

        self.smask.fill([180,220,255])

        if self.should_render_debug:
            self.world.render_debug(self.smask)
            pg.draw.line(self.smask,[255,100,100],[self.X/2,0],[self.X/2,self.Y])
            pg.draw.line(self.smask, [255, 100, 100], [0, self.Y/2], [self.X , self.Y/2])

        self.world.render(self.smask)

        scaled_smask = pg.transform.scale(self.smask,[self.screen.get_width(),
                                                      self.screen.get_height()])

        self.screen.blit(scaled_smask,[0,0])
        pg.display.update()


    def run(self):
        self.get_events()
        self.check_events()
        self.update_and_render()



