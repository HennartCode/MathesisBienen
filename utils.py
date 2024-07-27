import config
import pygame

# simuliert 8 weitere screens um den main screen herum (3x3 Feld)
# hier sind alle Abstandsberechnungen vom main screen zu diesen 8 Feldern
allDirections = [
    (0, 0),
    (-config.WIDTH, 0),
    (config.WIDTH, 0),
    (0, -config.HEIGHT),
    (0, config.HEIGHT),
    (-config.WIDTH, -config.HEIGHT),
    (-config.WIDTH, config.HEIGHT),
    (config.WIDTH, -config.HEIGHT),
    (config.WIDTH, config.HEIGHT),
]

# findet den kürzesten Vektor zwischen zwei Vektoren,
# dabei wird das Simulationsfeld als Torus behandelt
def nearestVector(pos1, pos2):
    """
        pos1: pygame.math.Vector2
        pos2: pygame.math.Vector2
        return: pygame.math.Vector2
    """
    global allDirections
    smallest = pos2 - pos1
    for x, y in allDirections:
        pos1.x += x
        pos1.y += y
        cur = pos2 - pos1
        if cur.length() < smallest.length():
            smallest = cur
    return smallest

# nimmt einen tuple mit zwei floats und macht diesen zu einem Vector
# error falls der tuple nicht genau floats (oder ints) hat
def tupleToVector2(t):
    """
        t: (float, float)
        return: pygame.math.Vector2
    """
    return pygame.math.Vector2(t[0], t[1])