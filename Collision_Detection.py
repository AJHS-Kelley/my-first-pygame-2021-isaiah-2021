# Pygame Collision Dection Practice, Isaiah Wright, January 11, 2022, 2:18pm
# Please review my added comments and fix the issues.  Thank you! - Mr. Kelley 

import pygame, sys, random
from pygame.locals import # add an * after import 

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

# Setup the player and food data structures.
foodCounter = 0
NEWFOOD = 400
FOODSIZE = 40
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(rabdom.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE)) 
                            # Typo above, should be random. )
# Movement Variables 
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if  event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key ==K_d:
                moveLeft = False 
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False 
                moveUP = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # Check to see if the player has stopped moving.                         
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key ==K_d:
                moveRight = False    
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False 
            if event.key == K_x: # Use x to teleport the player. 
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH -player.width) 

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1]), FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter => NEWFOOD: # Should be >= 
        # Add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE),FOODSIZE, FOODSIZE))

    # Draw while background on Window Surface.
    windowSurface.fill(WHITE)

    # move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED
    
    # Draw the player on the surface.
    pygame.draw.rect(windowSurface, BLACK, player)

    # Check for player colliding with food(s).
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # Draw the food.
     for i in range(len(foods)): # Move line one space to the right. 
         pygame.draw.rect(windowSurface, GREEN, foods[i]) # Move line one space to the right. 

    # Draw the window to the screen
    pygame.display.update()
    mainClock.tick(40)      






 