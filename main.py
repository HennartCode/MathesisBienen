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
state = config.MAIN


# sprite groups
all_sprites = pygame.sprite.Group()
bees = pygame.sprite.Group()
flowers = pygame.sprite.Group()
hives = pygame.sprite.Group()

# fonts
pause_text = pygame.font.SysFont('Comic Sans', 32).render('Pause', True, pygame.color.Color('White'))

"""
	fügt einen Sprite einer Gruppe hinzu und glechzeitig den Sprite
	zur Gruppe wo alle Sprites drinne sind
"""
def add_sprite(sprite, group):
    all_sprites.add(sprite)
    group.add(sprite)
    
for _ in range(2):
	add_sprite(hive.Hive(), hives)
for _ in range(50):
	add_sprite(bee.Bee(choice(hives.sprites()), random()-0.5, random()-0.5), bees)
f = flower.Flower()
add_sprite(f, flowers)

def main():
	global running
	global state
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p: state = config.PAUSE
				if event.key == pygame.K_s: state = config.MAIN
		if state == config.MAIN:
			screen.fill(config.BACKGROUND_COLOR)
			for bee in bees:
				bee.draw(screen)
			flowers.draw(screen)
			bees.update(f,bees)
			flowers.update(screen)
			hives.draw(screen)

		else:
			screen.blit(pause_text, (config.WIDTH - 100, 20))
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()

