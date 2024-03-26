import pygame as t
from sprites.plain import Plain
from sprites.balls import Ball
from sprites.block import Block

score = 0
t.font.init()
my_font = t.font.SysFont('Comic Sans MS', 30)

FPS = 100
t.init()
win = t.display.set_mode((750, 750))

all_sprites = t.sprite.Group()
plain = Plain(690, all_sprites)
balls = Ball(all_sprites)

blacks = t.sprite.Group()
for i in range(25):
    for J in range(3):
        Block(20 + 30 * i, 200 + 30 * J, 1, '#C2F83E', blacks, all_sprites)

    for j in range(3):
        Block(20 + 30 * i, 100 + 30 * j, 1, (165, 0, 165), blacks, all_sprites)

clock = t.time.Clock()
while True:
    for event in t.event.get():
        if event.type == t.QUIT:
            t.quit()
            exit()
    if balls.rect.colliderect(plain.rect):
        balls.collisions(plain.rect.center)
    b = t.sprite.spritecollide(balls, blacks, True, )
    if b is not None:
        if len(b) > 0:
            balls.block_collision(b[0].rect.center)
            score += 1
    sf = my_font.render(f'SCORE:{score}', False, (255,) * 3)
    all_sprites.update()
    win.fill((0,) * 3)
    all_sprites.draw(win)
    win.blit(sf, (0, 0))
    t.display.update()
    clock.tick(FPS)
