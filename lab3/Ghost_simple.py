import random as rnd
import numpy as np
import pygame
import pygame.draw as d
from PIL import Image

pygame.init()

FPS = 15
screen_width = 500
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
d.rect(screen, (150, 150, 150), (0, 0, 500, 700))

brown = (100, 30, 0)
pale_transparent = (215, 215, 255, 200)
black = (0, 0, 0)
white = (255, 255, 255)


# function takes only the shape of the ghost from image, else is done via pygame tools
def ghost(x, y, scale=1.0, orientation=True):
    if scale > 1:
        return print('error: scale <= 1')
    else:
        s = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        pixAr = pygame.PixelArray(s)
        A = []
        B = []
        with Image.open("ghostimage.png") as im:
            width, height = im.size
            for x_pix in range(width):
                for y_pix in range(height):
                    r, g, b, a = im.getpixel((x_pix, y_pix))
                    if r >= 10 and g >= 10 and b >= 10:
                        A.append(x + int(x_pix * scale))
                        B.append(y + int(y_pix * scale))
        print(len(A), len(B))
        for i in range(len(A)):
            pixAr[A[i]][B[i]] = pale_transparent
        del pixAr
        d.circle(s, (130, 130, 255), (x + int(75 * scale), y + int(35 * scale)), int(8 * scale))
        d.circle(s, (130, 130, 255), (x + int(108 * scale), y + int(30 * scale)), int(8 * scale))
        d.circle(s, black, (x + int(73 * scale), y + int(35 * scale)), int(4 * scale))
        d.circle(s, black, (x + int(106 * scale), y + int(30 * scale)), int(4 * scale))
        p = pygame.Surface((10, 4), pygame.SRCALPHA)
        d.ellipse(p, white, (0, 0, 10 * scale, 4 * scale))
        p = pygame.transform.rotate(p, 30)
        s.blit(p, (x + int(73 * scale), y + int(28 * scale)))
        s.blit(p, (x + int(106 * scale), y + int(23 * scale)))
        if not orientation:
            s = pygame.transform.flip(s, True, False)
        pygame.transform.scale(s, (int(screen_width * scale), int(screen_height * scale)))
        screen.blit(s, (0, 0))


def moon(x, y, R=75):
    d.circle(screen, (240, 240, 240), (x, y), R)
    for i in range(R // 3):
        randx = x + 1.4 * (rnd.random() - 0.5) * R
        randx = round(randx)
        randy = y + 1.4 * (rnd.random() - 0.5) * R
        randy = round(randy)
        d.circle(screen, (200, 200, 200), (randx, randy), 5 + round(5 * rnd.random()))


def cobweb(x, y, scale=1.0):
    R = 50 * scale
    for i in range(8):
        ymod = round(y + (R * np.sin(i * np.pi / 4)))
        xmod = round(x + (R * np.cos(i * np.pi / 4)))
        ymod_next = round(y + (R * np.sin((i - 1) * np.pi / 4)))
        xmod_next = round(x + (R * np.cos((i - 1) * np.pi / 4)))
        d.line(screen, (200, 255, 200), (x, y), (xmod, ymod))
        d.line(screen, (200, 255, 200), (xmod_next, ymod_next), (xmod, ymod))
        d.line(screen, (200, 255, 200), ((xmod + x) // 2, (ymod + y) // 2),
               ((xmod_next + x) // 2, (ymod_next + y) // 2))


# добавь паутину в 2-3 местах на доме
def house(x, y, scale=1.0):



def cloud(x, y, grayness=0.0, scale=1.0):
    s = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    d.ellipse(s, (255 * grayness, 255 * grayness, 255 * grayness, 100),
              (x, y, 120 * scale, 25 * scale))
    screen.blit(s, (0, 0))


moon(300, 100)
cloud(70, 100, grayness=0.8, scale=3)
cloud(90, 400, grayness=0.9, scale=2.2)
cobweb(150, 150, 0.5)
ghost(200, 200, orientation=False)
ghost(200, 200, 0.75)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
