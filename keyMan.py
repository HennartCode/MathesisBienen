import pygame
def key(event):
       
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_w:
                print(f"{ev.key}w")
            if event.key == pygame.K_a:
                print(f"{ev.key}a")
            if event.key == pygame.K_s:
                print(f"{ev.key}s")
            if event.key == pygame.K_d:
                print(f"{ev.key}d")