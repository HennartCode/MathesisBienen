import pygame
from random import randint
import config
'''
Hive()
Das Hive ist der Spawntpunkt von einer bestimmten Anzahl(config.BEES) an Bienen.
Sobald eine Biene ihr Blumenziehl erreicht hat, fliegt sie zu diesem zurück
'''
POLLENZIEL = 2 #neue Biene spwant wenn erreicht
class Hive(pygame.sprite.Sprite):
    def __init__(self,x,y,name):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.livingBees = config.BEES
        self.name = name
        self.data = [(0,0)]

    def dataUpdate(self,time):
        self.data.append((self.livingBees,time))

