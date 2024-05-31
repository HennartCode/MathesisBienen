import pygame
import config
import bee
import flower
import hive
from random import random, choice

pygame.init()
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()
running = True

def add_sprite(sprite, group):
    all_sprites.add(sprite)
    group.add(sprite)

# sprite groups
all_sprites = pygame.sprite.Group()
bees = pygame.sprite.Group()
flowers = pygame.sprite.Group()
hives = pygame.sprite.Group()

for _ in range(2):
	add_sprite(hive.Hive(), hives)
for _ in range(50):
	add_sprite(bee.Bee(choice(hives.sprites()), random(), random()), bees)
f = flower.Flower()
add_sprite(f, flowers)



def main():
	global running
	while running:
		screen.fill("purple")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for bee in bees:
			bee.draw(screen)
		flowers.draw(screen)
		bees.update(f)
		flowers.update(screen)
		hives.draw(screen)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()

