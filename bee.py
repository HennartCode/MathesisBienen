import pygame
import math
from random import randint

class Bee(pygame.sprite.Sprite):
    WIDTH, HEIGHT = 4, 4
    NEUTRAL_COLOR = (255, 255, 255)
    ATTRACTED_COLOR = "red"
    RETURN_COLOR = "green"
    SPEED = 1
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
    def update(self, flower, bees):

        scale = 3.0

        radius_repel = 3.0*scale
        radius_align = 25.0*scale
        radius_attract = 100.0*scale

        repel_strength = 1
        align_strength = 1
        social_strength = 1

        nearestBeeDistTo = float("inf")
        NearestBeeVecTo = pygame.Vector2(0.0,0.0)
        NearestBeeDir = pygame.Vector2(0.0,0.0)
        NearestBeeVel = 0
            
        ToFlower_vec = pygame.Vector2(0.0,0.0)
        ToHive_vec = pygame.Vector2(0.0,0.0)
        social_vec = pygame.Vector2(0.0,0.0)



        
        # Der Vektor von der Biene zur Blume
        to_flower = pygame.math.Vector2((flower.rect.center) - self.float_rect)
        _len = to_flower.length()

        # alle bienen durchgehen um nächste zu finden
        for bee in bees:
            BeeVecTo =  - self.float_rect + bee.float_rect #Vector zur gerade betrachteten Biene
            BeeDistTo = BeeVecTo.length()
            if BeeDistTo < nearestBeeDistTo and BeeDistTo > 0:
                NearestBeeVecTo = BeeVecTo
                nearestBeeDistTo = BeeDistTo
                NearestBeeDir = bee.dir
                NearestBeeVel = bee.SPEED


        if nearestBeeDistTo < radius_attract and nearestBeeDistTo > radius_align:
            social_vec = NearestBeeVecTo.normalize()

        if nearestBeeDistTo < radius_align and nearestBeeDistTo > radius_repel:
            social_vec = NearestBeeDir

        if nearestBeeDistTo < radius_repel:
            social_vec = -NearestBeeVecTo.normalize()

        # if math.isnan(social_vec):
        #     print("socialvec is NAN")
        #     exit()
        


        # falls der Vektor zur Blume <= des Blumen Radius entspricht
        # und die Biene neutral ist, fliegt die Biene zur Blume
        if _len <= Bee.RADIUS and self.status == "neutral":
            ToFlower_vec = to_flower/_len * min(_len, Bee.SPEED)
            self.image.fill(Bee.ATTRACTED_COLOR)
            
            # Ist sie nah genug dran, ändere den status und die Biene fliegt
            # zurück zum hive
            if _len < 5:
                self.status = "return"

        # Die Bewegung der Biene entschieden durch übergebene Argumente
        # während sie neutral ist 
        # elif self.status == "neutral":
            
        # Hier ist de Status return und die Biene fliegt zu ihrem hive zurück:
        # ['self.hive']
        elif self.status == "return": 
            self.image.fill(Bee.RETURN_COLOR)
            to_hive = pygame.math.Vector2((self.hive.rect.center) - self.float_rect)
            if to_hive.length() > 0:
                ToHive_vec = to_hive/to_hive.length() * min(to_hive.length(), Bee.SPEED)
        
        #Move Bee        
        social_vec *= social_strength
        self.dir = (self.dir + social_vec).normalize()

        self.float_rect += Bee.SPEED * self.dir



            

    def draw(self, screen):
        self.rect.center = (int(round(self.float_rect.x)), int(round(self.float_rect.y)))
        screen.blit(self.image, self.rect)
    
