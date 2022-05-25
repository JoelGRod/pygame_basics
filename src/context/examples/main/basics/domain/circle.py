import pygame
from pygame import Surface

import config.default as config

class Circle:
    def __init__(self, 
                 controller: pygame,
                 screen: Surface,
                 color: str,
                 position,
                 weight: int):
        self.controller = controller
        self.screen = screen
        self.color = color
        self.position = position
        self.weight = weight

    def draw(self):
        self.controller.draw.circle(
            self.screen, 
            config.colors[self.color], 
            self.position["start"], 
            self.position["radius"],
            self.weight
        )