import pygame
import config
import bee
import flower
import hive
from random import uniform
import time as time
import matplotlib.pyplot as plt
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
for hiveNum in range(config.HIVES):
    add_sprite(hive.Hive(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10),hiveNum),hives)
for i in range(config.BEES):
    for hive in hives:
        add_sprite(bee.Bee(hive, config.LEBENSDAUER), bees)
for i in range(config.FLOWERS):
    add_sprite(flower.Flower(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10)), flowers)

def main():
    global running
    global state
    startzeit = time.time()
    zeitintervall = 0
    #Gameloop:
    while running:
        '''
        Keypress
        '''
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
            #TODO: fix
            '''
            for hive in hives:
                if(hive.checkPollen()):
                    hive.addBee(bees)
            '''
            flowers.update(screen) 
            flowers.draw(screen)
            hives.draw(screen)
            
            curTime = time.time()
            if ((curTime-startzeit)>1):
                print("update")
                for hive in hives:
                    hive.dataUpdate(zeitintervall)
                    print(hive)
                startzeit = curTime
                zeitintervall += 1
        #PAUSE
        else:
            screen.blit(pause_text, (config.WIDTH - 100, 20))
        pygame.display.flip()
        clock.tick(60)
    #END
    for hive in hives:
        print(hive.name,hive.data)
        l1 = [x[0] for x in hive.data]
        l2 = [x[1] for x in hive.data]
        plt.plot(l1,l2)
    pygame.quit()
    plt.show()

if __name__ == "__main__":
     main()
