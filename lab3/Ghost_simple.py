import pygame
import pygame.draw as d
import random as rnd
import numpy as np

pygame.init()

FPS = 15
screen = pygame.display.set_mode((500, 700))
d.rect(screen, (150, 150, 150), (0, 0, 500, 700))

#нужен вложенный цикл с прозрачными поверхностями
def ghost():
    return None


def moon(x, y, R=75):
    d.circle(screen, (240, 240, 240), (x, y), R)
    for i in range(R // 3):
        randx = x + 1.4 * (rnd.random() - 0.5) * R
        randx = round(randx)
        randy = y + 1.4 * (rnd.random() - 0.5) * R
        randy = round(randy)
        d.circle(screen, (200, 200, 200), (randx, randy), 5 + round(5 * rnd.random()))


def cobweb(x, y, scale=1):
    R = 50 * scale
    for i in range(8):
        ymod = round(y + (R * np.sin(i * np.pi / 4)))
        xmod = round(x + (R * np.cos(i * np.pi / 4)))
        ymod_next = round(y + (R * np.sin((i - 1) * np.pi / 4)))
        xmod_next = round(x + (R * np.cos((i - 1) * np.pi / 4)))
        d.line(screen, (200, 255, 200), (x, y), (xmod, ymod))
        d.line(screen, (200, 255, 200), (xmod_next, ymod_next), (xmod, ymod))
        d.line(screen, (200, 255, 200), ((xmod+x)//2, (ymod+y)//2), ((xmod_next+x)//2, (ymod_next+y)//2))


#добавь паутину в 2-3 местах на доме
def house():
    return None


def cloud(x, y, grayness=0.0, scale=1):
    s = pygame.Surface((500, 700))
    s.set_alpha(128)
    s.fill((255, 255, 255))
    d.ellipse(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
              (x, y, 120 * scale, 25 * scale))
    screen.blit(s, (0, 0))


moon(300, 100)
cloud(70, 100, grayness=0.8, scale=3)
cobweb(150, 150, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
