import pygame
import bee
from random import uniform
'''
Die Blumen ziehen Bienen an.
Sobald die Biene das Zentrum erreicht erhält sie Nekter 
Geht gegebenfalls in 'RETURN'-State --> geht zurück zum Hive
'''
class Flower(pygame.sprite.Sprite):
    #konstante Werte
    WIDTH, HEIGHT = 20, 20
    COLOR = (0, 0, 0)

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface([Flower.WIDTH, Flower.HEIGHT])
        self.image.fill(Flower.COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pollen = uniform(20,30) 
        
    def update(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), self.rect.center, bee.Bee.RADIUS, width=2)
