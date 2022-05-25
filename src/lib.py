import pygame
from pygame import Surface

import config.default as config
from context.examples.main.animations.app.main_animations import Animations
from context.examples.main.basics.app.main_shapes import Shapes


class Game():
    def __init__(self, screen: Surface):
        self.screen = screen
        # 3º Clock
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.run()

    def run(self):
        # Animations
        animations = Animations(
            screen = self.screen, 
            color = config.colors["blue"]
        )
        basic_shapes = Shapes(
            screen = self.screen, 
            color = config.colors["black"]
        )
        
        # 4º Main Loop
        while(self.running):
            # 5º Exit Main Loop Logic
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                

            # 6º Screen Main Background color
            self.screen.fill(config.colors["white"])
            # Drawing in canvas

            ## Basic Draws
            basic_shapes.create_rectangle()
            basic_shapes.create_rectangles()

            ## Animations
            ## Square animated
            animations.animated_square()
            animations.animated_rain()
            ## Rain

            # End Animations


            # 7º Update Screen and Clock
            pygame.display.update()
            self.clock.tick(config.fps)
        