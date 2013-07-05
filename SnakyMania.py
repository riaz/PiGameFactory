#!/usr/bin/env python

import pygame,os
from pygame.locals import *

file_descr = os.path.split(os.path.abspath(__file__))
main_dir  = file_descr[0]
prog_name = file_descr[0]


def load_image(name):
    path = os.path.join(main_dir,name)
    return pygame.image.load(path).convert()

#main program
def main():
    pygame.init()
    size = [800,600]

    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('SnakyMania Demo')

    snake = load_image("snake.bmp")
    snakeRect = snake.get_rect()    
    screen.fill(black)
    screen.blit(snake,snakeRect)
    pygame.display.update()

    for x in range(150):
        screen.fill(black);
        snakeRect = snakeRect.move(4,0)
        screen.blit(snake,snakeRect)
        pygame.display.update();
        pygame.time.delay(100) 
    

if __name__ == '__main__': main()
