import pygame
import config

def torus_abs(pos1, pos2):
    """ 
        pos1: pygame.math.Vector2
        pos2: pygame.math.Vector2
        return: Float (Kleinster Abstand über Torus)
    """
    possible_distances = [
        (pos2 - pos1).length(),
        (pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y)).length(),
        (pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y)).length(),
        (pos2 - pygame.math.Vector2(pos1.x, pos1.y + config.HEIGHT)).length(),
        (pos2 - pygame.math.Vector2(pos1.x, pos1.y - config.HEIGHT)).length(),
        (pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y + config.HEIGHT)).length(),
        (pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y + config.HEIGHT)).length(),
        (pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y - config.HEIGHT)).length(),
        (pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y - config.HEIGHT)).length(),
    ]
    return min(possible_distances)
