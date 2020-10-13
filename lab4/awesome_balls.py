import pygame
import pygame.draw as d
import random as rnd

# Сделай дома через ооп

pygame.init()

FPS = 25
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
TRANSPARENT = (255, 255, 255, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
counter = 0


class Target(object):
    """
    Target object for "screen" plane. Can be moved and deleted
    """

    def __init__(self, r):
        max_r = r
        self.x = rnd.randint(max_r, screen_width - max_r)
        self.y = rnd.randint(max_r, screen_height - max_r)
        self.r = rnd.randint(15, max_r)
        self.color = COLORS[rnd.randint(0, 5)]
        self.v_x = rnd.randint(-velocity_max, velocity_max)
        self.v_y = rnd.randint(-velocity_max, velocity_max)

    def new_ball(self):
        """
        Creates a new ball

        :return: an image on "screen" plane
        """
        d.circle(screen, self.color, (self.x, self.y), self.r)

    def ball_movement(self):
        """
        Defines ball movement

        :return: an image on "screen" plane
        """
        if self.x > (screen_width - self.r):
            self.v_x = rnd.randint(-velocity_max, 0)
        elif self.x < self.r:
            self.v_x = rnd.randint(0, velocity_max)
        elif self.y < self.r:
            self.v_y = rnd.randint(0, velocity_max)
        elif self.y > (screen_height - self.r):
            self.v_y = rnd.randint(-velocity_max, 0)
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y
        d.circle(screen, self.color, (self.x, self.y), self.r)

    def ball_cords(self, cords: tuple):
        """
        Compares ball cords to given cords

        :return: bool type
        """
        if ((cords[0] - self.x)**2 + (cords[1] - self.y)**2) <= self.r**2:
            return True
        else:
            return False

    def target_exterminate(self):
        """
        Makes Target disappear
        """
        self.x, self.y = 2000, 2000

    def new_star(self):
        """
        Creates a new Star

        :return: an image on "screen" plane
        """
        temp_surf = pygame.Surface((2*self.r, 2*self.r))
        temp_surf.fill(TRANSPARENT)
        d.polygon(temp_surf, self.color, ((self.r, 0), (self.r + self.r//5, self.r - self.r//5), (2*self.r, self.r),
                                          (self.r + self.r//5, self.r + self.r//5), (self.r, 2*self.r),
                                          (self.r - self.r//5, self.r + self.r//5), (0, self.r),
                                          (self.r - self.r//5, self.r - self.r//5), (self.r, 0)))
        temp_surf.set_colorkey(TRANSPARENT)
        screen.blit(temp_surf, (self.x + self.r, self.y + self.r))

    def star_movement(self):
        """
        Defines star movement

        :return: an image on "screen" plane
        """
        if self.x > (screen_width - 3*self.r):
            self.v_x = rnd.randint(-velocity_max, 0)
        elif self.x < -self.r:
            self.v_x = rnd.randint(0, velocity_max)
        elif self.y < -self.r:
            self.v_y = rnd.randint(0, velocity_max)
        elif self.y > (screen_height - 3*self.r):
            self.v_y = rnd.randint(-velocity_max, 0)
        self.x = self.x + self.v_x
        self.y = self.y + self.v_y
        temp_surf = pygame.Surface((2*self.r, 2*self.r))
        temp_surf.fill(TRANSPARENT)
        d.polygon(temp_surf, self.color, ((self.r, 0), (self.r + self.r//5, self.r - self.r//5), (2*self.r, self.r),
                                          (self.r + self.r//5, self.r + self.r//5), (self.r, 2*self.r),
                                          (self.r - self.r//5, self.r + self.r//5), (0, self.r),
                                          (self.r - self.r//5, self.r - self.r//5), (self.r, 0)))
        temp_surf.set_colorkey(TRANSPARENT)
        screen.blit(temp_surf, (self.x + self.r, self.y + self.r))

    def star_cords(self, cords: tuple):
        """
        Compares star cords to given cords

        :return: bool type
        """
        if ((cords[0] - self.x - 2*self.r)**2 + (cords[1] - self.y - 2*self.r)**2) <= (self.r//2)**2:
            return True
        else:
            return False


circle_1 = Target(max_ball_r)
circle_2 = Target(max_ball_r)
obj_3 = Target(max_ball_r)
restart = 0
player_score = 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('FINAL SCORE:', player_score)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if circle_1.ball_cords(pygame.mouse.get_pos()):
                circle_1.target_exterminate()
                restart += 1
                player_score += 1
            if circle_2.ball_cords(pygame.mouse.get_pos()):
                circle_2.target_exterminate()
                restart += 1
                player_score += 1
            if obj_3.star_cords(pygame.mouse.get_pos()):
                obj_3.target_exterminate()
                restart += 3
                player_score += 3
            if restart % 5 == 0:
                if restart != 0:
                    counter = 0

    if counter < 4*FPS and counter != 0:
        screen.fill(BLACK)
        circle_1.ball_movement()
        circle_2.ball_movement()
        obj_3.star_movement()
        counter += 1
        screen.blit(text_score, (5, 5))
        pygame.display.update()
    else:
        screen.fill(BLACK)
        counter = 0
        restart = 0
        circle_1 = Target(max_ball_r)
        circle_2 = Target(max_ball_r)
        obj_3 = Target(max_ball_r)
        counter = 1
        player_score_str = str(player_score)
        f1 = pygame.font.Font(None, 72)
        text_score = f1.render(player_score_str, 0, RED)
        screen.blit(text_score, (5, 5))
        pygame.display.update()


pygame.quit()
