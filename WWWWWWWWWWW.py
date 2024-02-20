import pygame as t

t.init()
FPS = 120

W, H = 500, 500
win = t.display.set_mode((500, 500))
clock = t.time.Clock()

t.display.set_caption('PYGAME')

def  random_color():
    import random
    return random.choices(range(256),k=4)









# while 1 always true
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()




    x,y=t.mouse.get_pos()
    if t.key.get_pressed()[t.K_SPACE]:
        win.fill((1,)*3)

    t.draw.circle(win,random_color(),(x,y),25)
    t.display.update()
    clock.tick(FPS)