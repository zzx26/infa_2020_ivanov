import pygame
import pygame.draw as d
import random as rnd

pygame.init()

FPS = 15
screen = pygame.display.set_mode((500, 700))
d.rect(screen, (150, 150, 150), (0, 0, 500, 700))


def ghost():
    return None


def moon():
    return None


def house():
    return None


def cloud(x, y, grayness=0.0, scale=1):
    d.ellipse(screen, (255 * grayness, 255 * grayness, 255 * grayness, 255 * (1 - grayness)),
              (x, y, 120 * scale, 25 * scale))


cloud(50, 50, grayness=0.2, scale=3)
cloud(70, 100, grayness=0.9, scale=3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
