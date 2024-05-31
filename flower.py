import pygame
import bee
import config

class Flower(pygame.sprite.Sprite):
	WIDTH, HEIGHT = 20, 20
	COLOR = (0, 0, 0)
	SPEED = 2

	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([Flower.WIDTH, Flower.HEIGHT])
		self.image.fill(Flower.COLOR)
		self.rect = self.image.get_rect()
		self.rect.x = config.WIDTH - bee.Bee.RADIUS - Flower.WIDTH
		self.rect.y = config.HEIGHT - bee.Bee.RADIUS - Flower.HEIGHT

	def update(self, screen):
		pygame.draw.circle(screen, (0, 0, 0), self.rect.center, bee.Bee.RADIUS, width=2)
		self.rect.y -= Flower.SPEED
