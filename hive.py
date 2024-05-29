import pygame
from random import randint
import config

class Hive(pygame.sprite.Sprite):
	RADIUS 
	
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([20, 20])
		self.image.fill((100, 100, 100))
		self.rect = self.image.get_rect()
		self.rect.x = randint(0, config.WIDTH)
		self.rect.y = randint(0, config.HEIGHT) 
	
