import pygame
import gridrules
from random import randint
from array import *
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_RETURN,
    K_BACKSPACE,
    K_r,
    K_g,
    K_i
)

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BUTTON_HEIGHT = 0
CELL_WIDTH = 20

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gridrules.initGrid(SCREEN_WIDTH, SCREEN_HEIGHT-BUTTON_HEIGHT, CELL_WIDTH)

# Fill the screen with white
screen.fill((255, 255, 255))

# Variable to keep the main loop running
running = True

surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT-BUTTON_HEIGHT))



def printGrid():

    for row in range(gridrules.h):
        for cell in range(gridrules.w):
            ract = pygame.Rect(cell*CELL_WIDTH, row*CELL_WIDTH, CELL_WIDTH,CELL_WIDTH)

            if(gridrules.gridTable[row, cell] == 1):
                pygame.draw.rect(surf, (255,90,127), ract)

            elif(gridrules.gridTable[row, cell] == 0):
                pygame.draw.rect(surf, (255,255,255), ract)

    for i in range(gridrules.h+1):
        pygame.draw.line(surf, (200,200,200), (0,i*CELL_WIDTH), (SCREEN_WIDTH, i*CELL_WIDTH))
    for i in range(gridrules.w+1):
        pygame.draw.line(surf, (200,200,200), (i*CELL_WIDTH, 0), (i*CELL_WIDTH, SCREEN_HEIGHT))
    screen.blit(surf, (0,BUTTON_HEIGHT))
    pygame.display.flip()


run = False
glider = False

for i in range(gridrules.w):
    gridrules.clickGrid(i, int(gridrules.h/2))

printGrid()
# Main loop
while running:
    # Look at every event in the queue

    if run:
        gridrules.incGrid()
        printGrid()

    for event in pygame.event.get():
        # Did the user hit a key?
        printGrid()
        if event.type == pygame.MOUSEBUTTONUP:
            if(event.pos[1] > 50):

                if(glider):
                    glider = False
                    gridrules.glider(int(event.pos[0]/CELL_WIDTH), int((event.pos[1]-BUTTON_HEIGHT)/CELL_WIDTH))
                else:
                    gridrules.clickGrid(int(event.pos[0]/CELL_WIDTH), int((event.pos[1]-BUTTON_HEIGHT)/CELL_WIDTH))
                    printGrid()

        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RETURN:
                run = not run
            elif event.key == K_BACKSPACE:
                run = False
                gridrules.clear()
            elif event.key == K_i:
                gridrules.incGrid()
            elif event.key == K_r:
                gridrules.initRandom()
            elif event.key == K_g:
                glider = True
            printGrid()
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
