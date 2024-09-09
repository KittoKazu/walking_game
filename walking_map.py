import pygame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 764
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_img = pygame.image.load('sprites_and_art/cat.png')
map_img = pygame.image.load('sprites_and_art/cool.png')
WHITE = (255, 255, 255)

def init_map():

    pygame.init()
    screen.blit(map_img, (0, 0))
    #screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)

def use_player(x,y):
    screen.blit(player_img,(x, y))

def update_map():
    screen.blit(map_img, (0, 0))
