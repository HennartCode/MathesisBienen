import pygame
import config
import bee
import flower
import hive
from random import uniform
import time as time
import matplotlib.pyplot as plt

#Init-Routine
pygame.init()#intialisiert pygame
pygame.display.set_caption('Bienen Simulation')
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))#Bildschirm-Grösse
clock = pygame.time.Clock()

running = True
state = config.MAIN

"""
    Spritegruppen:
    jedes Objekt, welches auf dem Bildschirm zu sehen ist, gehört zu einer Sprite-Gruppe und erben von dem
    pygame.Sprite-Objekt, welches draw und update Funktionen liefert
    Dies macht das Arbeiten mit Hives,Bees etc. uebersichtlicher
"""
#initialisieren der sprite groups
all_sprites = pygame.sprite.Group()
bees = pygame.sprite.Group()
flowers = pygame.sprite.Group()
hives = pygame.sprite.Group()

#initialisieren der fonts
pause_text = pygame.font.SysFont('Comic Sans', 32).render('Pause', True, pygame.color.Color('White'))

"""
    fügt einen Sprite einer Gruppe hinzu und glechzeitig den Sprite
    zur Gruppe in welcher sich alle Sprites befinden
"""
def add_sprite(sprite, group):
    all_sprites.add(sprite)
    group.add(sprite)

'''
    Hives, deren Bienen und Blumen werden zu Spritegruppen hinzugefügt
'''
for hiveNum in range(config.HIVES):
    add_sprite(hive.Hive(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10),hiveNum),hives)
for i in range(config.BEES):
    for hive in hives:
        add_sprite(bee.Bee(hive, config.LEBENSDAUER), bees)
for i in range(config.FLOWERS):
    add_sprite(flower.Flower(uniform(10,config.WIDTH-10),uniform(10,config.HEIGHT-10)), flowers)

'''
    Main
    Ist verantwortlich fuer die ganze Simulation, hier werden alle Objekte aktualisiert/gezeichnet
    Keypress-Aktionen überwacht und ausgewertet
    Matplotlib am Ende der Simulation aufgerufen
'''
def main():
    global running
    global state
    #wichtige Variblen --> Intervall für Matplotlib
    startzeit = time.time()
    zeitintervall = 0

    #Gameloop:
    while running:
        '''
            Der Eventmanager ist für alle möglichen Eingaben über die Tastatur verantwortlich:
            - Mit 'p' wird die Simulation entweder pausiert oder fortgesetzt
            Glechzeitig wird schliessen der Simulation ohne Fehlermeldung ermoeglicht.
        '''
        #eventmanager
        for event in pygame.event.get():
            #Quit
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                #'p'-Taste gedrueckt
                if event.key == pygame.K_p:
                    #Pause
                    if state == config.MAIN:
                        state = config.PAUSE
                    #Continue
                    elif state == config.PAUSE:
                        state = config.MAIN
        #RUNNING
        if state == config.MAIN:
            screen.fill(config.BACKGROUND_COLOR)
            #malen für jede Biene --> draw() funktioniert nicht mit bees-Gruppe
            for bee in bees:
                bee.draw(screen)

            #update für jede Blume
            for flower in flowers:
                bees.update(flower,bees)
            #restliche Sprite-Gruppen updaten und darstellen
            flowers.update(screen)
            flowers.draw(screen)
            hives.draw(screen)

            '''
                In einem Intervall von einer Sekunde wird von jedem Hive in der Sprite-Gruppe Hives
                die Anzahl der lebenden Bienen und der Zeitpunkt in einen Array uebergeben und gespeichert
            '''
            curTime = time.time()#aktuelle Zeit
            if ((curTime-startzeit)>1):#wird jede Sekunde aufgerufen
                for hive in hives:#methode für jedes Hive aufgerufen
                    hive.dataUpdate(zeitintervall)
                startzeit = curTime#Zeit wird aktualisiert
                zeitintervall += 1
        #PAUSE
        else:
            screen.blit(pause_text, (config.WIDTH - 100, 20))
        pygame.display.flip()
        clock.tick(60)
    #END
    '''
        Hive-Daten werden mit Matplotlib auf das selbe Koordinatensystem geplottet
    '''
    #Matplotlib/Auswertung
    for hive in hives:
        l1 = [x[0] for x in hive.data]
        l2 = [x[1] for x in hive.data]
        plt.plot(l1,l2)#plotten jeweiliger Daten
    pygame.quit()#Pygame wird geschlossen
    plt.show()#Graphen anzeigen

'''
    main() wird bei start des Programms aufgerufen
'''
if __name__ == "__main__":
    main()

