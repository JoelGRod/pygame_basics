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


# ? Suggested Game Structures
'''
Option I - Small Games
src/
    lib.py -> Main Manager
    app.py
    context/
        game_name_1/ -> Domain + Domain module
            main/
                game_name_1_manager.py -> Game Manager
                levels/
                characters/
                styles/
                animations/
                etc...
            tests/
        game_name_2/
        game_name_3/
        ...
        shared/
            main/
            tests/

Option II - Big Game
src/
    lib.py                      -> Main Manager
    app.py                      -> Config Init
    context/
        game_name/              -> Domain
            main/
                game_manager.py -> Game Manager
                main_menu/
                level_1/        -> Domain Module
                level_2/
                level_3/
                ...
                shared/
            tests/
        shared/
            main/
            tests/

Option III - Big Game (Not recommended)
src/
    lib.py -> Main Manager / Game Manager
    app.py
    context/
        level_1/ -> Domain + Domain module
            main/
            tests/
        level_2/
        level_3/
        level_4/
        ...
        shared/
            main/
            tests/
'''