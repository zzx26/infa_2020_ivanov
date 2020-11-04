from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса Ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 2
        self.bounce = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600). После нескольких отражений от стен убирает мяч
        """
        if self.x >= 800 - self.r or self.x <= self.r:
            self.vx = -self.vx
            self.bounce += 1
        if self.y >= 600 - self.r or self.y <= self.r:
            self.vy = -self.vy
            self.bounce += 1
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.ay
        if self.bounce >= 3:
            self.x = self.y = 3000
            self.vx = self.vy = self.ay = 0
        self.set_coords()

    def collision(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2) < (self.r + obj.r)**2:
            return True
        else:
            return False


class Sting(Ball):
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 2
        self.bounce = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_line(40, 450, 40 + 2*self.vx, 450 - 2*self.vy, width=3)
        self.live = 30

    def set_coords(self):
        canv.coords(self.id, self.x, self.y, self.x + 2*self.vx, self.y - 2*self.vy)

    def move(self):
        if self.x >= 800 - self.r or self.x <= self.r:
            self.vx = -self.vx
            self.bounce += 1
        if self.y >= 600 - self.r or self.y <= self.r:
            self.vy = -self.vy
            self.bounce += 1
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.ay
        self.vx = round(self.vx*(1 + 0.1*rnd(-3, 4)))
        if self.bounce >= 3:
            self.x = self.y = 3000
            self.vx = self.vy = self.ay = 0
        self.set_coords()


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.x = 20
        self.y = 450
        self.v = 3
        self.id_base = canv.create_rectangle(self.x - 20, self.y + 20, self.x + 20, self.y, fill='green')
        self.id = canv.create_line(20, 450, self.x + 30, self.x - 30, width=7, fill='red')

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        coin_flip = rnd(0, 2)
        if coin_flip == 0:
            new_ball = Ball()
        else:
            new_ball = Sting()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def aiming(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - self.y) / (event.x - self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def set_coords(self):
        canv.coords(self.id_base, self.x - 20, self.y + 20, self.x + 20, self.y)
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an))

    def move_left(self, event=0):
        if event:
            self.x -= self.v
            self.set_coords()

    def move_right(self, event=0):
        if event:
            self.x += self.v
            self.set_coords()


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.vx = rnd(-3, 3)
        self.vy = rnd(-3, 3)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.vx = self.vy = 0
        self.x = self.y = 2500
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение цели за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, и стен по краям окна (размер окна 800х600).
        """
        if self.x >= 800 - self.r or self.x <= self.r:
            self.vx = -self.vx
        if self.y >= 600 - self.r or self.y <= self.r:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()


t1 = Target()
t2 = Target()
t3 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global Gun, t1, screen1, balls, bullet
    t1.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.aiming)
    canv.bind('<a>', g1.move_left)
    canv.bind('<d>', g1.move_right)

    z = 0.03
    t1.live = 1
    while t1.live or t2.live or t3.live or balls:
        for b in balls:
            b.move()
            t1.move()
            t2.move()
            t3.move()
            if b.collision(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.collision(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if b.collision(t3) and t3.live:
                t3.live = 0
                t3.hit()
            if t1.live == t2.live == t3.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.bind('<a>', '')
                canv.bind('<d>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(z)
        g1.aiming()
        g1.power_up()
        g1.move_left()
        g1.move_right()
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(750, new_game)


new_game()
root.mainloop()
