import pygame
import math
from random import randint

class Bee(pygame.sprite.Sprite):
    WIDTH, HEIGHT = 20, 20
    NEUTRAL_COLOR = (255, 255, 255)
    ATTRACTED_COLOR = "red"
    RETURN_COLOR = "green"
    speed = 5
    RADIUS = 100
    MAX_SPEED = 10 #m/s**2

    def __init__(self, hive, dir_x, dir_y):
        super().__init__()
        self.image = pygame.Surface([Bee.WIDTH, Bee.HEIGHT])
        self.image.fill(Bee.NEUTRAL_COLOR)
        self.rect = self.image.get_rect()
        self.hive = hive	
        self.rect.x = hive.rect.x
        self.rect.y = hive.rect.y
        self.dir = pygame.math.Vector2(dir_x, dir_y).normalize()
        #Placeholder
        if (Bee.speed > Bee.MAX_SPEED):
            Bee.speed = BEE.MAX_SPEED
        """
            Speichert die Position der Biene als Float, wichtig für interne
            Verarbeitung, ['self.rect'] wird intern von pygame benutzt, dafür
            rundet man ['self.float_rect'] zu Integern, siehe Methode ['self.draw']
        """
        self.float_rect = pygame.math.Vector2(self.rect.x, self.rect.y)
        """
            status:
                neutral => war noch bei keiner Blume
                return => war bei der Blume und kehrt zum hive zurück
        """
        self.status = "neutral" # todo make it enum

    """
        Das Verhalten der Bienen wird mit dieser Methode jedes Frame aktualisiert/ausgeführt.
        Die Biene spawnt an dem ihr zugewiesenen Hive und fliegt in eine vorgegebene Richtung.
            ACHTUNG: Momentan wird der Hive und die Flugrichtung zufällig in ['main.py'] entschieden.
        Sobald sie im Radius einer Blume kommt, verfärbt sie sich rot und fliegt zur Blume.
        Anschließend wird sie grün und fliegt zu ihrem Hive zurück.
    """
    def update(self, flower):
        # Der Vektor von der Biene zur Blume
        to_flower = pygame.math.Vector2((flower.rect.center) - self.float_rect)
        _len = to_flower.length()
        
        # falls der Vektor zur Blume <= des Blumen Radius entspricht
        # und die Biene neutral ist, fliegt die Biene zur Blume
        if _len <= Bee.RADIUS and self.status == "neutral":
            self.float_rect += to_flower/_len * min(_len, Bee.speed)
            self.image.fill(Bee.ATTRACTED_COLOR)
            
            # Ist sie nah genug dran, ändere den status und die Biene fliegt
            # zurück zum hive
            if _len < 5:
                self.status = "return"
        
        # Die Bewegung der Biene entschieden durch übergebene Argumente
        # während sie neutral ist 
        elif self.status == "neutral":
            self.float_rect.x += Bee.SPEED * self.dir.x
            self.float_rect.y += Bee.SPEED * self.dir.y
            
        # Hier ist de Status return und die Biene fliegt zu ihrem hive zurück:
        # ['self.hive']
        else:
            self.image.fill(Bee.RETURN_COLOR)
            to_hive = pygame.math.Vector2((self.hive.rect.center) - self.float_rect)
            if to_hive.length() > 0:
                self.float_rect += to_hive/to_hive.length() * min(to_hive.length(), Bee.SPEED)

    def draw(self, screen):
        self.rect.center = (int(round(self.float_rect.x)), int(round(self.float_rect.y)))
        screen.blit(self.image, self.rect)

