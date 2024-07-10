import pygame
import config
import bee
import flower
import hive
from random import random, choice, uniform
import time as time

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
for i in range(config.HIVES):
    add_sprite(hive.Hive(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10),i),hives)
for i in range(config.BEES):
    add_sprite(bee.Bee(choice(hives.sprites()), config.LEBENSDAUER), bees)
for i in range(config.FLOWERS):
    add_sprite(flower.Flower(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10)), flowers)
def main():
    global running
    global state
    startzeit = time.time()
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
        #RUNNING
        if state == config.MAIN:
            screen.fill(config.BACKGROUND_COLOR)
            for bee in bees:
                bee.draw(screen)

            for flower in flowers:
                bees.update(flower,bees)

            flowers.update(screen) 
            flowers.draw(screen)
            hives.draw(screen)
            
            curTime =time.time()
            if (curTime-startzeit>=30):
                for hive in hives:
                    hive.dataUpdate()
                    startzeit = curTime
        #PAUSE
        else:
            screen.blit(pause_text, (config.WIDTH - 100, 20))
        pygame.display.flip()
        clock.tick(60)
    for hive in hives:
        print(hive.data)
    pygame.quit()

if __name__ == "__main__":
    main()
