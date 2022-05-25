import pygame
from pygame import Surface

from context.examples.main.shared.aggregates import (
    Position, 
    Dimensions, 
    Speed,
    Color
)

class Square:
    def __init__(
        self, 
        screen: Surface,
        position: Position,
        dimensions: Dimensions,
        speed: Speed,
        color: Color
        ) -> None:
        # Animated square coordinates
        self.x_pos, self.y_pos = position.x, position.y
        self.width, self.height, self.weight = (
            dimensions.width, 
            dimensions.height, 
            dimensions.weight
        )
        self.x_speed, self.y_speed = speed.x, speed.y
        self.color = color.color
        # Controllers
        self.screen = screen

    def update(self):
        if self.x_pos >= 700 or self.x_pos <= 0:
            self.x_speed *= -1
        if self.y_pos >= 400 or self.y_pos <= 0:
            self.y_speed *= -1
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def draw(self):
        pygame.draw.rect(
            self.screen, 
            self.color, 
            (self.x_pos, self.y_pos, self.width, self.height), 
            self.weight
        )
