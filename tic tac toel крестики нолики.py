import pygame as t

t.init()
FPS =1000
BLACK=(0,)*3
GRAY=(100,)*3
WHITE=(255,)*3
RED=(255,0,0)
YELLOW=(255,255,0)
LG=(0,200,200)
CROSS='#046582'
CIRCLE='#e4bad4'
W, H = 500, 500




win = t.display.set_mode((500, 500))
clock = t.time.Clock()
class Board:
    def __init__(self,w,h,size):
        pass

    def click(self,mouse_pos):
        pass

    def render(self,screen):
        pass

t.display.set_caption('PYGAME')



clock=t.time.CLock()
board=Board(W,H,200)
# while 1 always true
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()
        if event.type == t.MOUSEBUTTONDOWN:
            board.click(event.pos)



    win.fill(WHITE)
    board.render(win)
    t.display.update()

    keys=t.key.get_pressed()
    if keys[t.K_ESCAPE]:
        t.quit()
        exit()
    clock.tick(FPS)