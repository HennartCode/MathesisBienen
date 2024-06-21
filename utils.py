import pygame
import config

# findet den kürzesten Vektor zwischen zwei Vektoren,
# dabei wird das Simulationsfeld als Torus behandelt
def neartest_vector(pos1, pos2):
    """
        pos1: pygame.math.Vector2
        pos2: pygame.math.Vector2
        return: pygame.math.Vector2
    """
    possible_vectors = [
        pos2 - pos1,
        pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y),
        pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y),
        pos2 - pygame.math.Vector2(pos1.x, pos1.y + config.HEIGHT),
        pos2 - pygame.math.Vector2(pos1.x, pos1.y - config.HEIGHT),
        pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y + config.HEIGHT),
        pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y + config.HEIGHT),
        pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y - config.HEIGHT),
        pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y - config.HEIGHT),
    ]
    return min(possible_vectors, key = lambda v: v.length())
