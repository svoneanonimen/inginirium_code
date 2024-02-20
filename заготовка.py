import pygame as t

t.init()
FPS = 120

W, H = 500, 500
win = t.display.set_mode((500, 500))
clock = t.time.Clock()

t.display.set_caption('PYGAME')

# while 1 always true
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()
    clock.tick(FPS)


