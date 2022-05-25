import pygame, random

from pygame import Surface

from context.examples.main.shared.aggregates import (
    Speed,
    Color
)

class Rain:
    def __init__(
        self, 
        screen : Surface, 
        color: Color, 
        speed: Speed,
        intensity: int) -> None:

        self.screen = screen
        self.color = color.color
        self.x_speed, self.y_speed = speed.x, speed.y
        self.intensity = intensity
        self.rain_coords = []

        self.create_rain()

    def create_rain(self) -> None:
        for drop in range(self.intensity):
            x = random.randint(1, 800)
            y = random.randint(0, 600)
            self.rain_coords.append([x, y])

    def draw_update(self) -> None:
        for drop in self.rain_coords:
            pygame.draw.circle(
                self.screen, 
                self.color, 
                drop, 
                1
            )
            self.update(drop)

    def update(self, drop: list[int, int]) -> None:
        drop[0] += self.x_speed
        drop[1] += self.y_speed
        if drop[0] >= 800: drop[0] = 0
        elif drop[1] >= 600: drop[1] = 0