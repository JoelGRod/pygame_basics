import pygame
from pygame import Surface

import config.default as config

class Line:
    def __init__(self, 
                 controller: pygame,
                 screen: Surface):
        self.controller = controller
        self.screen = screen
        self.color = color
        self.position = position
        self.weight = weight

    def draw(self):
        self.controller.draw.line(
            self.screen, 
            config.colors[self.color], 
            self.position["start"], 
            self.position["end"],
            self.weight
        )