import pygame
from pygame import Surface

import config.default as config
from context.examples.main.examples_manager import ExamplesManager

class Game():
    def __init__(self, screen: Surface):
        self.screen = screen
        # * 3º Clock
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.run()

    def run(self):
        # * 4º Main Loop
        while(self.running):
            # * 5º Exit Main Loop Logic
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
                

            # * 6º Screen Main Background color
            self.screen.fill(config.colors["white"])

            # Domain Games (user selection here)
            ExamplesManager(self)

            # * 7º Update Screen and Clock
            pygame.display.update()
            self.clock.tick(config.fps)
