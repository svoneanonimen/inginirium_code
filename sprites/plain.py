import pygame as t


class Plain(t.sprite.Sprite):
    def __init__(self, y, *groups):
        super().__init__(*groups)
        self.image = t.Surface((150, 20))
        self.image.fill((255, 255, 155))
        self.rect = self.image.get_rect()
        self.rect.y = 690
        self.rect.x = 370

    def update(self):
        x, _ = t.mouse.get_pos()
        self.rect.x = x - 75

