import pygame
import math
from random import randint

class Bee(pygame.sprite.Sprite):
	WIDTH, HEIGHT = 20, 20
	NEUTRAL_COLOR = (255, 255, 255)
	ATTRACTED_COLOR = "red"
	RETURN_COLOR = "green"
	SPEED = 5
	RADIUS = 100

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
		self.status = "neutral" # todo make it enum
		

	def update(self, flower):
		delta_vec = pygame.math.Vector2((flower.rect.center) - self.float_rect)
		_len = deltaVec.length()
		if _len <= Bee.RADIUS and self.status == "neutral":
			self.float_rect += delta_vec/_len * min(_len, Bee.SPEED))
			self.image.fill(Bee.ATTRACTED_COLOR)
			if _len < 5:
				self.status = "return"
		elif self.status == "neutral":
			self.float_rect.x += Bee.SPEED * self.dir.x
			self.float_rect.y += Bee.SPEED * self.dir.y
		else: 
			self.image.fill(Bee.RETURN_COLOR)
			delta_hive = pygame.math.Vector2((self.hive.rect.center) - self.float_rect)
			if delta_hive.length() > 0:
				self.float_rect += delta_hive/delta_hive.length() * min(delta_hive.length(), Bee.SPEED)

	def draw(self, screen):
		self.rect.center = (int(round(self.float_rect.x)), int(round(self.float_rect.y)))
		screen.blit(self.image, self.rect)
	
