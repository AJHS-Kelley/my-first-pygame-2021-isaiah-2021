# My First PyGame, Isaiah Wright, 11/29/21 2:28pm, v0.0

import pygame, sys
from pygame.locals import *
# start PyGame
pygame.init()

# setup our window. 1
windowsurface = pygame.display.set_mode((500, 400), 0, 32) 
pygame.display.set_caption('hello, world')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 225, 225)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup font.
basicfont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicfont.render('hello, World', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centrax
textRect.centery = windowSurface.get_rect().centery