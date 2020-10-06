import pygame
import pygame.draw as d
import random as rnd

pygame.init()

FPS = 120
screen_width = 1100
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
max_ball_r = 75
velocity_max = 10

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(max_r: int):
    """
    рисует новый шарик
    contains all variables in tuple
    """
    x = rnd.randint(max_r, screen_width - max_r)
    y = rnd.randint(max_r, screen_height - max_r)
    r = rnd.randint(10, max_r)
    color = COLORS[rnd.randint(0, 5)]
    v_x = rnd.randint(-velocity_max, velocity_max)
    v_y = rnd.randint(-velocity_max, velocity_max)
    d.circle(screen, color, (x, y), r)
    new_ball.data = (x, y, r, color, v_x, v_y)


def ball_movement(init_ball_data: tuple):
    """
    creates movement of a given ball
    """
    x = init_ball_data[0]
    y = init_ball_data[1]
    r = init_ball_data[2]
    color = init_ball_data[3]
    v_x = init_ball_data[4]
    v_y = init_ball_data[5]
    for i in range(FPS*2):
        clock.tick(FPS)
        x = v_x + x
        y = v_y + y
        d.circle(screen, color, (x, y), r)
        pygame.display.update()
        screen.fill(BLACK)

        if x < r:
            v_x = rnd.randint(0, velocity_max)
            v_y = rnd.randint(-velocity_max, velocity_max)
        elif x > (screen_width - r):
            v_x = rnd.randint(-velocity_max, 0)
            v_y = rnd.randint(-velocity_max, velocity_max)
        elif y < r:
            v_y = rnd.randint(0, velocity_max)
            v_x = rnd.randint(-velocity_max, velocity_max)
        elif y > (screen_height - r):
            v_y = rnd.randint(-velocity_max, 0)
            v_x = rnd.randint(-velocity_max, velocity_max)


def ball_object(data, max_r: int):
    """
    создает newballом шарик, двигает и перерисовывает movementом
    :return:
    """
    return None


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')

    new_ball(max_ball_r)
    ball_movement(new_ball.data)

pygame.quit()
