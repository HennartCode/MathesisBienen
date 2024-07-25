"""
    Alle oberflaechlichen Veraendrungen der Simulation koennen hier gesteuert werden.
"""
#---General---
WIDTH, HEIGHT = 900, 900
MAIN, PAUSE = 1, 0
BACKGROUND_COLOR = "gray"

#---Spielfeld---
#Anzahl der Objecte hier festlegen
BEES = 200 #pro Hive
HIVES = 5
FLOWERS = 3
HINDERNISSE = 0 #TODO hindernisse hinzufuegen

#---Bienen---
#wie lange Bienen leben
LEBENSDAUER = 10 #in sekunden

#---Extra---
ENDLESS=True #Bienen bewegen sich zu naechster Blume,wenn sie den Hive erreicht haben
IGNOREOTHERS=True #Bienen ignorieren alle Bienen welche nicht im selben Zustand wie Biene selbst sind
