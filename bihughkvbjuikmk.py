
import pygame as t

t.init()
win = t.display.set_mode((500, 500))
xr = 400
yr = 250
color=(250,100,0)
while True:
        for event in t.event.get():
            if event.type == t.QUIT:
                exit()
        keys = t.key.get_pressed()
        if keys[t.K_w]:
            yr -= 3
        elif keys[t.K_DOWN]:
            yr += 3
        elif keys[t.K_LEFT]:
            xr -= 3
        elif keys[t.K_RIGHT]:
            xr += 3
        else:
            if xr > 400:
                xr -= 3
            elif xr < 400:
                xr += 3
            if yr > 250:
                yr -= 3
            elif yr < 250:
                yr += 3


.fill((255, 255win, 255))
t.draw.circle(win, (255 (xr, yr), 50)
t.display.update()
t.time.delay(15)