import pygame
from pygame import Surface

from context.examples.main.shared.aggregates import (
    Position, 
    Dimensions,
    Color
)

class Rectangle:
    def __init__(self,
                 screen: Surface,
                 position: Position,
                 dimensions: Dimensions,
                 color: Color):
        self.x_pos, self.y_pos = position.x, position.y
        self.width, self.height, self.weight = (
            dimensions.width, 
            dimensions.height, 
            dimensions.weight
        )
        self.color = color.color
        self.screen = screen

    def draw(self):
        pygame.draw.rect(
            self.screen, 
            self.color, 
            (self.x_pos, self.y_pos, self.width, self.height),
            self.weight
        )
    
    def draw_rects(self, step: int):
        for x in range(self.x_pos, self.screen.get_width(), step):
            pygame.draw.rect(
                self.screen, 
                self.color,
                (x - self.width / 2, self.y_pos, self.width, self.height),
                self.weight
            )