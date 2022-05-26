import pygame

import config.default as config
from context.examples.main.animations.app.main_animations import Animations
from context.examples.main.basics.app.main_shapes import Shapes

class ExamplesManager:
    def __init__(self, controller) -> None:
        self.screen = controller.screen
        self.clock = controller.clock
        self.examples_running = True
        # * Manager Run
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
        while(self.examples_running):
            # 5º Exit Main Loop Logic
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.examples_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.examples_running = False
            
            # Screen Main Background color
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