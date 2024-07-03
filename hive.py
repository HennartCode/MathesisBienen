import pygame
from random import randint
import config

class Hive(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface([20, 20])
		self.image.fill((100, 100, 100))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
