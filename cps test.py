# sys to manipulate different parts of the Python Runtime Environment
import sys

import pygame
# imports all the available pygame modules into the pygame package
# source for learning pygame module: https://www.javatpoint.com/pygame
from pygame.locals import *

# initialise colours based off rgb
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
# initialise variables
clicks = 0
running = True
# initialise pygame source: https://www.pygame.org/docs/ref/pygame.html
pygame.init()
pygame.font.init()
# initialise display
screen_size = screen_width, screen_height = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Nathanael Thie - CPS TEST')
myfont = pygame.font.SysFont('calibri', 30)
fnt_12 = pygame.font.SysFont('calibri', 12)



Fps = 60
clock = pygame.time.Clock() #built-in timer
first_click = False
nxt_time = 0.000001 # cannot be 0 since we cannot divide a value by 0, and clicks per second relies on dividing by time elapsed
print(pygame.font.get_fonts())  # refernece to see which fonts can be chosen



# while the program is running
while running:

    for event in pygame.event.get(): # get events from the queue
        if event.type == QUIT:
            quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: # when the left mouse button gets clicked
            if first_click == False: # if we havnet clicked the screen yet, then the timer will start
                first_click = True
                clicks += 1
            elif (first_click == True): # while timer is below 5 secs it will increminent clicks
                if nxt_time < 5:
                    clicks += 1

            # tried to draw a circle at mouse position whenever screen is clicked - however not working
            # pygame.draw.circle(screen, pygame.Color(0, 0, 255), pygame.mouse.get_pos(), 20, 2)

        if event.type == pygame.KEYDOWN: #check if keydown event occurred
            #check if escape key was pressed - terminate program
            if event.key == pygame.K_ESCAPE:
                print('Terminating program')
                event.type = QUIT
            # check is space key or tab key was pressed - to restart program
            if event.key == pygame.K_SPACE or event.key == pygame.K_TAB:
                first_click = False
                nxt_time = 0.000001
                clicks = 0

    if first_click == True and nxt_time < 5:
        nxt_time += clock.tick_busy_loop() / 1000

    # draw text source: https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

    # initialise the text displayed = args: (text, antialias, colour, background)
    textsurface_title = myfont.render("CPS Test - 5 seconds", True, white)
    textsurface_clicks = myfont.render("Clicks: " + str(clicks), True, white)
    textsurface_time = myfont.render("Time: " + str(round(nxt_time, 4)), True, white)
    textsurface_cps = myfont.render("Clicks per second: " + str(round(clicks / nxt_time, 4)), True, white)
    textsurface_help_1 = fnt_12.render("Press Tab or Space to restart" , True, white)
    textsurface_help_2 = fnt_12.render("Press Escape to quit program" , True, white)


    screen.fill(black)


    # positions of text
    screen.blit(textsurface_title, (150, 10))
    screen.blit(textsurface_clicks, (0, 100))
    screen.blit(textsurface_time, (0, 150))
    screen.blit(textsurface_cps, (0, 200))
    screen.blit(textsurface_help_1, (0, 350))
    screen.blit(textsurface_help_2, (0, 370))

    pygame.display.update() # Update portions of the screen for software displays

# PROBLEMS ENCOUNTERED

# spent alot of time trying to utilise in-built commands from pygame module instead of taking the hard coding alternative
# mostly initialising and making sure no errors in syntax, since learning commands from a new module is alienating without tutorials
# the algorithm to calculating clicks per second is easy

# FURTHER IDEAS

# make option to choose time limit so maybe option to choose 1 secs, 5 secs, 10 secs, 30 secs, instead of only 5 secs
# make visually appealing
