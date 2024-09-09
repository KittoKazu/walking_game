import pygame
import walking_map

speed = 2
pygame.key.set_repeat(1,1)

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def moving(x,y):
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        y -= speed
    if key[pygame.K_s]:
        y += speed
    if key[pygame.K_a]:
        x -= speed
    if key[pygame.K_d]:
        x += speed
    return x,y
