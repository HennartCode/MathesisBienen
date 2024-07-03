import config

t = [
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
def nearest_vector(pos1, pos2):
    """
        pos1: pygame.math.Vector2
        pos2: pygame.math.Vector2
        return: pygame.math.Vector2
    """
    global t
    # possible_vectors = [
    #     pos2 - pos1,
    #     pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y),
    #     pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y),
    #     pos2 - pygame.math.Vector2(pos1.x, pos1.y + config.HEIGHT),
    #     pos2 - pygame.math.Vector2(pos1.x, pos1.y - config.HEIGHT),
    #     pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y + config.HEIGHT),
    #     pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y + config.HEIGHT),
    #     pos2 - pygame.math.Vector2(pos1.x - config.WIDTH, pos1.y - config.HEIGHT),
    #     pos2 - pygame.math.Vector2(pos1.x + config.WIDTH, pos1.y - config.HEIGHT),
    # ]
    # return min(possible_vectors, key = lambda v: v.length())

    smallest = pos2 - pos1
    for x, y in t:
        pos1.x += x
        pos1.y += y
        cur = pos2 - pos1
        if cur.length() < smallest.length():
            smallest = cur
    return smallest
