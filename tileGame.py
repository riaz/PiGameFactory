import pygame
import os
import sys

tiles = 20

if os.path.isfile("tree.bmp"):
    tree = pygame.image.load("tree.bmp") 
else:
    print("Cannot find file: tree.bmp",stderr)

if os.path.isfile("hero.bmp"):
    hero = pygame.image.load("hero.bmp")
    
else:
    print("Cannot find file: hero.bmp",stderr)    

size = [800,600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('First tile game')

playerPos = 0

def background_render(tiles):
   background = [tree]*tiles
   for i in range(tiles):
       screen.blit(background[i],(i*40,0))

#background = [tree,tree,tree,tree,tree,tree,tree]
#for i in range(7):
#    print(i)
#    screen.blit(background[i],(i*50,0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    if playerPos < tiles:                    
        ##################
        #background = [tree]*tiles
        #for i in range(tiles):
        #    screen.blit(background[i],(i*40,0))
        ##################
        background_render(tiles)                
        screen.blit(hero,(playerPos*40,0))
        pygame.time.wait(500)
        playerPos = playerPos + 1
        pygame.display.flip()
    else:
        playerPos = 0
