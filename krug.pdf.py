import pygame as t


class Circle:
    def __init__(self, color, x, y, rad):
        self.col = color
        self.x = x
        self.y = y
        self.rad = rad
        self.is_jump=False
        self.h=100
    def move_by_keys(self):
        if self.is_jump:
            if self.h >=-100:
                self.y-=self.h

                self.h-=50
            else:
                self.h=100
                self.is_jump=False
        keys = t.key.get_pressed()
        if keys[t.K_w]:
            self.y -= 3
        elif keys[t.K_s]:
            self.y += 3
        if keys[t.K_d]:
            self.x += 3
        elif keys[t.K_a]:
            self.x -= 3
        if keys[t.K_SPACE]:
            self.is_jump=True



    def draw(self, root):
        t.draw.circle(root, self.col, (self.x, self.y), self.rad)

circle=Circle((100,50,250),250,250,25)
t.init()
win = t.display.set_mode((600,600))
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            exit()
    circle.move_by_keys()
    win.fill((255, 255, 255))
    circle.draw(win)
    t.display.update()
    t.time.delay(10)
