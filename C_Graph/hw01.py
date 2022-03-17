
import pygame
from sys import exit
import numpy as np

width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolylineMouseButton")

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

old_pt = np.array([0, 0])
cur_pt = np.array([0, 0])
count = 0

# screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
pressed = -1
margin = 6


mouse_click = []
past_pressed = 0

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 2
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = -1

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    cur_pt = [x, y]

    if pressed == 2 and past_pressed == 1:
        mouse_click.append(cur_pt)
        count += 1
        pygame.draw.rect(screen, BLUE, (cur_pt[0] - margin, cur_pt[1] - margin, margin * 2, margin * 2), 4)

    #print("mouse x:" + repr(x) + " y:" + repr(y) + " button:" + repr(button1) + " " + repr(button2) + " " + repr(button3) + " pressed:" + repr(pressed))
    old_pt = cur_pt

  
    if len(mouse_click) >= 2:
        for i in range(count - 1):
            pygame.draw.line(screen, GREEN, mouse_click[i], mouse_click[i + 1], 3)

    past_pressed = pressed
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()

pygame.quit()
