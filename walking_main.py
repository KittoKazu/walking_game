import walking_inputs
import walking_map
import walking_map as map
import walking_inputs as inputs
import pygame

def main():
    x = 200
    y = 200
    map.init_map()
    walking_map.use_player(x,y)
    pygame.display.set_caption('Walking game')
    while True:
        walking_map.update_map()
        inputs.check_events()
        speed = walking_inputs.sprint()
        x,y = walking_inputs.moving(x,y,speed)
        walking_map.use_player(x,y)
        pygame.display.update()


if __name__ == '__main__':
    main()