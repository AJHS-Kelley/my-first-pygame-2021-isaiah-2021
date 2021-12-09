# Simple Animation with pyGame, isaiah wright, 12/09/21, 2:33 pm v0.5

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.init()

# Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'    

MOVESPEED = 4

# Setup color values
WHITE =(255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setup the box data. 
b1 = {'react':pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir':UPRIGHT}
b2 = {'react':pygame.Rect(200, 200, 20, 20), 'color': GREEN, 'dir':UPLEFT}
b3 = {'react':pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Run the game loop.
while True:
    # Check for Quit event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()