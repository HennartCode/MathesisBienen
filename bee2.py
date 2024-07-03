import pygame
import config
import groups


class Bee(pygame.sprite.Sprite):
    WIDTH, HEIGHT = 5, 5
    NEUTRAL_COLOR = "white"

    def __init__(self, hive, dir_x, dir_y):
        super().__init__()
        self.image = pygame.Surface([Bee.WIDTH, Bee.HEIGHT])
        self.image.fill(Bee.NEUTRAL_COLOR)
        self.rect = self.image.get_rect()
        self.hive = hive
        self.rect.x = hive.rect.x
        self.rect.y = hive.rect.y
        self.dir = pygame.math.Vector2(dir_x, dir_y).normalize()
        self.float_rect = pygame.math.Vector2(self.rect.x, self.rect.y)

    def update(self):
         
