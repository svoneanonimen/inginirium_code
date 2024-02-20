import pygame as p

p.init()

w, h = [int(t) for t in input().split()]
win = p.display.set_mode((w, h))
#win.fill((255,255,255))
#p.draw.circle(win
win.fill = ((0, 0, 0))
p.draw.line(win,(100,100,100),(0,0), (w,h),5)
p.draw.line(win,(100,100,100),(w,0), (0,h),5)
p.display.update
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            exit()
