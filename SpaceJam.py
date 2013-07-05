#!/usr/bin/env python

"""
This example shows us how to move objects in space
"""

import pygame,os
from pygame.locals import *

file_descr = os.path.split(os.path.abspath(__file__))
main_dir  = file_descr[0]
prog_name = file_descr[1]

#game object Class
class GameObject:
    def __init__(self,image,height,speed):
        self.speed = speed
        self.image = image
        self.pos   = image.get_rect().move(0,height)
    def move(self):
        self.pos = self.pos.move(self.speed,0)
        if self.pos.right > 760:
            self.pos.left = 0
            
#quick function to load an image
def load_image(name):
    path = os.path.join(main_dir,name)
    return pygame.image.load(path).convert()
    
#main program
def main():
    pygame.init()
    size = [800,600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("SpaceJam Demo")

    player = load_image("ufo.bmp")
    background = load_image("space.bmp")

    # scaling the background to fill the screen
    background = pygame.transform.scale(background,size)   

    screen.blit(background,(0,0))

    objects = [] # to keep track of GameObject instances

    for x in range(10): # to init,assign image,speed,x and y component to obj
        o = GameObject(player,x*50,x)
        objects.append(o)

    while 1:
        for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN):
                return
        # code to erase objects in previous position
        for o in objects:
            screen.blit(background,o.pos,o.pos)
        #code to move and blit objects in new position
        for o in objects:
            o.move()
            screen.blit(o.image,o.pos)
        pygame.display.update()

if __name__ == '__main__': main()
    

