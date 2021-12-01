# My First PyGame, Isaiah Wright, 11/29/21 2:28pm, v0.0

import pygame, sys
from pygame import pixelarray
from pygame.locals import *
# start PyGame
pygame.init()

# setup our window. 1
windowSurface = pygame.display.set_mode((500, 400), 0, 32) 
pygame.display.set_caption('hello, world')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 225, 225)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CRIMSONRED = (122, 0, 0)

# Setup font.
basicfont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicfont.render('hello, World', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# fill background color.
windowSurface.fill(CRIMSONRED)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, CRIMSONRED, ((146, 0), (291, 106), (56, 277), (0, 106)))

# Draw lines on the screen
pygame.draw.line(windowSurface, BLACK,(60,60), (120, 60), 4)
pygame.draw.line(windowSurface, WHITE,(75,60), (120, 75), 2)
pygame.draw.line(windowSurface, RED,(0,60), (120, 0), 1)

#Draw a circle
pygame.draw.circle(windowSurface, BLACK, (300, 50), 20, 0)

#Draw an ellipse
pygame.draw.ellipse(windowSurface, RED, (300, 50), 20, 0)

#Draw the text rectangle
pygame.draw.rect(windowSurface, RED,(textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

#create pygame.PixelArray
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][360] = BLUE
del pixArray

# Draw the text onto the surface
windowSurface.blit(text, textRect)

#update pygame display
pygame.display.update()

#Run game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()