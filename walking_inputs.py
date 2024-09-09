import pygame
import walking_map

pygame.key.set_repeat(1,1)

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def sprint():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        speed = 5
    else:
        speed = 2
    return speed

def moving(x,y,speed):
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
