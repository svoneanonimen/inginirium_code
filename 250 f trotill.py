import pygame as t
import random
t.init()
win = t.display.set_mode((500, 500))


class Circle:
    def __init__(self, color, x, y, rad):
        self.col = color
        self.x = x
        self.y = y
        self.rad = rad
        self.dir = 'r'

    def horizont_move(self):
        if self.x > 500 - self.rad:
            self.dir = 'l'
        elif self.x < 0 + self.rad:
            self.dir = "r"
        if self.dir == 'r':
            self.x +=10
        elif self.dir == 'l':
            self.x -= 10


    def draw(self, root):
        t.draw.circle(root, self.col, (self.x, self.y), self.rad)

FPS=120
clock=t.time.Clock()


circles = []
for i in range(999):
    circles.append(Circle(random.choices(range(256), k=3), i * 10, i * 5, 30))

while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()
    for i in range(999):
        circles[i].horizont_move()
    win.fill((255, 255, 255))
    for i in range(999):
        circles[i].draw(win)

    t.display.update()
    t.time.delay(10)
