import pygame
import config
import groups
from enum import Enum
from random import randint, random
import flower

Status = Enum("Status", ["NEUTRAL", "ATTRACTED", "RETURN"])


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
        self.dir = pygame.math.Vector2(random(), random())
        self.float_rect = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.status = Status
        self.polls = 0

    def update(self):
        if self.status == Status.NEUTRAL:
            min_flower_distance: pygame.math.Vector2 = min(
                groups.flowers, key=lambda f: (f.float_rect - self.float_rect).length()
            )
            if self.polls == 3:
                self.status = Status.RETURN
                self.dir = self.hive.float_rect - self.float_rect
            elif min_flower_distance <= flower.Flower.RADIUS:
                self.status = Status.ATTRACTED
                self.dir = min_flower_distance

        if self.status == Status.ATTRACTED and :


        self.float_rect += Bee.SPEED * self.dir

    def draw(self, screen):
        self.rect.center = (
            int(round(self.float_rect.x)),
            int(round(self.float_rect.y)),
        )
        screen.blit(self.image, self.rect)
