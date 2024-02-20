import pygame as t

t.init()
win = t.display.set_mode((950,650))
xr = 249
yr = 249
color = (250, 250, 0)
speed=(8)
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            exit()
    if xr>=400 or xr <=150 or yr>=400 or yr<=150:
        speed=(8)
    else:
        speed=(3)
    keys = t.key.get_pressed()
    if keys[t.K_UP]  :
        yr -= speed
    elif keys[t.K_DOWN] :
        yr += speed
    elif keys[t.K_LEFT] :
        xr -= speed
    elif keys[t.K_RIGHT]:
        xr += speed
    else:
        if xr != 400:
            xr += (250 - xr) / abs(250 - xr) * 3
        if yr != 250:
            yr += (250 - yr) / abs(250 - yr) * 3
    if xr >= 400 or xr <= 150 or yr >= 400 or yr <= 100:
        color = (250, 0, 0)
    else:
        color = (250, 250, 0)

    win.fill((255, 255, 255))
    t.draw.circle(win, color, (xr, yr), 50)
    t.display.update()
    t.time.delay(15)
