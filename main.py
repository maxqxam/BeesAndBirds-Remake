import pygame as pg
from pygame.locals import *

from Game import Game

pg.init()
X,Y = 1000,750
main_screen = pg.display.set_mode((X,Y),RESIZABLE)
fps = 30
clock = pg.time.Clock()

game = Game(main_screen)

while not game.is_over:
    game.run()
    clock.tick(fps)













