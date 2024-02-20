import pygame as t
import random

t.init()

FPS = 1000


GRAY = (75,) * 3
W, H = 500, 500
win = t.display.set_mode((500, 500))
clock = t.time.Clock()

t.display.set_caption('PYGAME')


class Star:
    def __init__(self):
        self.x, self.y = t.mouse.get_pos()
        self.color = (255,) * 3

    def self_draw(self, root):
        t.draw.circle(root, self.color, (self.x, self.y), 10)

    def dark(self):
        if self.color[0] > 0:
            self.color = (self.color[0] - 1,) * 3


stars = []

# while 1 always true
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()
    if t.mouse.get_pressed()[0]:
        stars.append(Star())

    for star in stars:
        star.self_draw(win)
        star.dark()

    for _ in range(10):
        t.draw.circle(win, GRAY, (random.randint(0, W), random.randint(0, H)), 10)
    t.display.update()
    clock.tick(FPS)
