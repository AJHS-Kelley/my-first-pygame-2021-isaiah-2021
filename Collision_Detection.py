# Pygame Collision Dection Practice, Isaiah Wright, January 07, 2022, 2:00pm

import pygame, sys, random
from pygame.locals import 

# Setup Pygame
pygame.init()
mainClock = pygame.time.Clock()

# Setup the Pygame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Collision Detection 2022')

# Setup colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


