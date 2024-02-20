import pygame as t

t.init()
win = t.display.set_mode((500, 500))
xc = 10
yc = 10
xr = 20
yr = 10
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            exit()

    yc = yc + 5
    xc = xc
    yr = yr
    xr = xr + 5
    if yc + 5 < 0:
        yc = 500
    if yc - 5 > 500:
        yc = 0
    if xr - 5 < 0:
        xr = 500
    if xr + 5 > 500:
        xr = 0

    win.fill((255, 255, 255))
    t.draw.rect(win, (255, 255, 0), (xr, yr, 50, 80))
    t.draw.circle(win, (255, 255, 0), (xc, yc), 50)
    t.display.update()
    t.time.delay(15)
