import pygame
import config.default as config

# Main Game
from lib import Game

def main():
    # Config
    # 1º Engine Init
    pygame.init()
    # 2º Screen Config
    screen = pygame.display.set_mode(config.screen_size)
    # Images and sounds
    # image = pygame.image.load("foo.png").convert # Use convert_alpha() for images with transparency
    Game(screen = screen)
    # 8º Exit Game
    pygame.quit()


if __name__ == "__main__":
    main()