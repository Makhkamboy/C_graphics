"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
    
width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode((width, height), 0, 32)

background_image_filename = 'image/curve_image.png'

background = pygame.image.load(background_image_filename).convert()
width, height = background.get_size()
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("ImagePolylineMouseButton")
font = pygame.font.SysFont("arial",16)


# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pta = [300,200]
ptb = [200,300]
ptc = [400,350]

pts = []
knots = []
count = 0
#screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=3):
    # pygame.draw.line(screen, color, pt, pt)
    pygame.draw.circle(screen, color, pt, thick)

#HW2 implement drawLine with drawPoint
def drawLine(pt0, pt1, color='GREEN', thick=3):
    x = pt0[0]
    y = pt0[1]
    x1 = pt0[0]
    y1 = pt0[1]
    x2 = pt1[0]
    y2 = pt1[1]

    dx = abs(x2-x1)
    dy = abs(y2-y1)
    gradient = dy/dx

    if gradient >1:
        dx,dy = dy,dx
        x , y = y , x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx

    for k in range(dx):
        x = x+1 if x < x2 else x-1
        if p>0:
            y = y+1 if y < y2 else y -1
            p = p+2*(dy-dx)
        else:
            p = p+2*dy

        if gradient < 1:
            drawPoint([x, y], color, thick)
        else:
            drawPoint([y, x], color, thick)
    # drawPoint((100,100), color,  thick)
    # drawPoint(pt0, color, thick)
    # drawPoint(pt1, color, thick)

def drawPolylines(color='GREEN', thick=3):
    if(count < 2 ): return
    for i in range(count-1):
        drawLine(pts[i], pts[i+1], color,thick)
        #pygame.draw.line(screen, color, pts[i], pts[i+1], thick)

def barycentric(pta,ptb,ptc,p):
    sx = np.array([ptb[0] - pta[0],ptc[0]-pta[0],pta[0]-p[0]])
    sy = np.array([ptb[1] - pta[1],ptc[1]-pta[1],pta[1]-p[1]])

    u = np.cross(sx,sy)
    return  1 - (u[0] + u[1]) / u[2], u[0] / u[2], u[1] / u[2]


#Loop until the user clicks the close button.
done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0

pygame.draw.rect(screen, BLUE, (pta[0] - margin, pta[1] - margin, 2 * margin, 2 * margin), 5)
pygame.draw.rect(screen, BLUE, (ptb[0] - margin, ptb[1] - margin, 2 * margin, 2 * margin), 5)
pygame.draw.rect(screen, BLUE, (ptc[0] - margin, ptc[1] - margin, 2 * margin, 2 * margin), 5)
drawLine(pta, ptb, GREEN, 1)
drawLine(pta, ptc, GREEN, 1)
drawLine(ptb, ptc, GREEN, 1)

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = -1
        elif event.type == pygame.MOUSEBUTTONUP:
            pressed = 1
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = [x, y]

    a,b,c = barycentric(pta,ptb,ptc,pt)
    print("pt mouse x:" + repr(x) + " y:" + repr(y) + " --(" + repr(a) + " ," + repr(b) + " ," + repr(c)+")")
    pygame.draw.circle(screen, BLACK, pt, 3)

    
    pygame.display.update()
    old_button1 = button1
    old_pressed = pressed

pygame.quit()

