import pygame
import config
import bee
import flower
import hive
from random import random, choice, uniform

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


'''
Hives, deren Bienen und Blumen werden zu Spritegruppe hinzugefügt
'''
for _ in range(config.HIVES):
    add_sprite(hive.Hive(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10)),hives)
for _ in range(config.BEES):
    add_sprite(bee.Bee(choice(hives.sprites()), random(), random()), bees)
for i in range(config.FLOWERS):
    add_sprite(flower.Flower(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10)), flowers)

'''
prop_flower = flower.Flower()
add_sprite(prop_flower, flowers)
'''

def main():
    global running
    global state
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if state == config.MAIN:
                        state = config.PAUSE
                    elif state == config.PAUSE:
                        state = config.MAIN

        if state == config.MAIN:
            screen.fill(config.BACKGROUND_COLOR)
            for bee in bees:
                bee.draw(screen)
            flowers.draw(screen)
            #bees.update(flowers,bees)
            for f in flowers:
                bees.update(f,bees)
                #bees.update(prop_flower_list[1],bees)
            flowers.update(screen)
            hives.draw(screen)

        else:
            screen.blit(pause_text, (config.WIDTH - 100, 20))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()

