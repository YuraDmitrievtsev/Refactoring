import numpy as np

import pygame
from pygame.draw import *


pygame.init()

FPS = 30
L=1800
W=900
screen = pygame.display.set_mode((L, W))

#colors
WHITE = (255, 255, 255)
RED=(200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
DARK_GRAY=(251, 251, 251)
VERY_LIGHT_BLUE=(0, 250, 250)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
LIGHT_GREEN=(0, 204, 0)
YELLOW = (225, 225, 0)
DARK_YELLOW=(204, 204, 0)
PINK = (230, 50, 230)
ORANGE=(255,165,0)
BLUE=(0, 76, 153)
BROWN=(165,42,42)
DARK_BROWN=(204, 102, 0)
LIGHT_BROWN=(255, 153, 51)
STRANGE_GREEN=(153, 153, 9)
DARK_GREEN=(0, 102, 51)

#Sky
screen.fill(VERY_LIGHT_BLUE)

#ground
rect(screen, LIGHT_GREEN, (0, W//2, L, W//2))

def circle_with_circuit(sc,x,y,r,internal_color):
    circle(sc, BLACK, (x, y), r+5)
    circle(sc, internal_color, (x, y), r)

def draw_tree(x,y,s):
    l=300*s
    w=495*s
    screen_current = pygame.Surface((l, w))
    screen_current.fill(YELLOW)
    screen_current.set_colorkey(YELLOW)
    rect(screen_current, BLACK, (s * 135, s * 275, s * 40, s * 220))

    Radius=70
    circle_with_circuit(screen_current, np.int(s*155), np.int(s* 75), np.int(s*Radius), DARK_GREEN)
    circle_with_circuit(screen_current, np.int(s* 85), np.int(s* 85), np.int(s*Radius), DARK_GREEN)
    circle_with_circuit(screen_current, np.int(s*205), np.int(s*125), np.int(s*Radius), DARK_GREEN)
    circle_with_circuit(screen_current, np.int(s*155), np.int(s*195), np.int(s*Radius), DARK_GREEN)
    circle_with_circuit(screen_current, np.int(s*225), np.int(s*245), np.int(s*Radius), DARK_GREEN)
    circle_with_circuit(screen_current, np.int(s* 75), np.int(s*185), np.int(s*Radius), DARK_GREEN)
    circle_with_circuit(screen_current, np.int(s*105), np.int(s*235), np.int(s*Radius), DARK_GREEN)

    screen.blit(screen_current,(x,y))

def draw_cloud(x,y,s):
    l = 320*s
    w = 190*s
    screen_current = pygame.Surface((l, w))
    screen_current.fill(YELLOW)
    screen_current.set_colorkey(YELLOW)

    Radius=np.int(60*s)
    circle_with_circuit(screen_current, np.int( 65*s), np.int(115*s), Radius, DARK_GRAY)
    circle_with_circuit(screen_current, np.int(115*s), np.int(115*s), Radius, DARK_GRAY)
    circle_with_circuit(screen_current, np.int(185*s), np.int(125*s), Radius, DARK_GRAY)
    circle_with_circuit(screen_current, np.int(255*s), np.int(115*s), Radius, DARK_GRAY)
    circle_with_circuit(screen_current, np.int(215*s), np.int( 85*s), Radius, DARK_GRAY)
    circle_with_circuit(screen_current, np.int(135*s), np.int( 65*s), Radius, DARK_GRAY)

    screen.blit(screen_current, (x, y))

def draw_house(x,y,s):
    l = 450 * s
    w = 450 * s
    screen_current = pygame.Surface((l, w))
    screen_current.fill(YELLOW)
    screen_current.set_colorkey(YELLOW)

    # walls
    rect(screen_current, BLACK, (np.int(s * 34), np.int(s * 182), np.int(s * 356), np.int(s * 256)))
    rect(screen_current, DARK_BROWN, (np.int(s * 37), np.int(s * 185), np.int(s * 350), np.int(s * 250)))

    # roof
    polygon(screen_current, BLACK,
            [(np.int(s *   0), np.int(s * 185)),
             (np.int(s * 424), np.int(s * 185)),
             (np.int(s * 212), np.int(s *   0))])
    polygon(screen_current, LIGHT_BROWN,
            [(np.int(s *   7), np.int(s * 182)),
             (np.int(s * 417), np.int(s * 182)),
             (np.int(s * 212), np.int(s *   5))])

    # window
    rect(screen_current, STRANGE_GREEN, (np.int(s * 137), np.int(s * 245), np.int(s * 80), np.int(s * 100)))
    rect(screen_current, BLUE, (np.int(s * 142), np.int(s * 250), np.int(s * 70), np.int(s * 90)))


    screen.blit(screen_current, (x, y))

def draw_Sun(x,y,s):
    l = 450 * s
    w = 450 * s
    screen_current = pygame.Surface((l, w))
    screen_current.fill(YELLOW)
    screen_current.set_colorkey(YELLOW)

    n = 18  # spikes
    for theta in range(0, n, 1):
        t = 2 * (3.1415926535) / n

        x = 1590 + 50 * np.cos(t * theta)
        y = 100 + 50 * np.sin(t * theta)

        x1 = 1590 + 50 * np.cos(t * (theta + 1))
        y1 = 100 + 50 * np.sin(t * (theta + 1))

        x2 = 1590 + 60 * np.cos(t * (theta + 0.5))
        y2 = 100 + 60 * np.sin(t * (theta + 0.5))

        polygon(screen, DARK_YELLOW, [(x, y), (x1, y1), (x2, y2)])

    circle(screen, YELLOW, (1590, 100), 50)

    screen.blit(screen_current, (x, y))

draw_Sun(0,0,1)

draw_house(200,300,0.5)
draw_house(600,300,0.5)
draw_cloud(200,100,0.7)
draw_cloud(600,100,1)
draw_cloud(1200,100,0.5)
draw_tree(100,300,0.5)
draw_tree(500,400,0.7)
draw_tree(800,300,1)
draw_house(1000,400,1)



pygame.display.update()

finished = False

clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()