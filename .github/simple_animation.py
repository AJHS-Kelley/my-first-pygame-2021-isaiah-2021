# Simple Animation with pyGame, isaiah wright, 12/09/21, 1:31 pm

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.init()

# Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')
