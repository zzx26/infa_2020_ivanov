import pygame
import pygame.draw as d

pygame.init()

FPS = 15
screen = pygame.display.set_mode((400, 400))

d.rect(screen, (150, 150, 150), (0, 0, 400, 400))
d.circle(screen, (255, 255, 0), (200, 200), 150)

d.circle(screen, (255, 0, 0), (150, 150), 30)
d.circle(screen, (255, 0, 0), (250, 150), 30)
d.circle(screen, (0, 0, 0), (150, 150), 15)
d.circle(screen, (0, 0, 0), (250, 150), 15)
d.rect(screen, (0, 0, 0), (130, 280, 140, 20))

d.polygon(screen, (0, 0, 0), [(110, 110), (110, 95), (190, 140)])
d.polygon(screen, (0, 0, 0), [(110, 95), (190, 125), (190, 140)])

d.polygon(screen, (0, 0, 0), [(400 - 110, 110), (400 - 110, 95), (400 - 190, 140)])
d.polygon(screen, (0, 0, 0), [(400 - 110, 95), (400 - 190, 125), (400 - 190, 140)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
