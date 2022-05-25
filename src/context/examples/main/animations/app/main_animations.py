from pygame import Surface

from context.examples.main.animations.domain import (
    Square, 
    Rain
)

from context.examples.main.shared.aggregates import (
    Position, 
    Dimensions, 
    Speed, 
    Color
)

class Animations:
    def __init__(self, screen: Surface, color: tuple[int, ...]) -> None:
        self.screen = screen
        self.color = Color(color)
        self.square = self.create_square()
        self.rain = self.create_rain()

    def create_square(self) -> Square:
        return Square(
            screen = self.screen, 
            position = Position(x = 300, y = 300), 
            dimensions = Dimensions(width = 100, height = 100, weight = 5), 
            speed = Speed(x = 2, y = 2),
            color = self.color
        )
    
    def animated_square(self) -> None:
        self.square.update()
        self.square.draw()

    def create_rain(self) -> Rain:
        return Rain(
            screen = self.screen,
            color = self.color,
            speed = Speed(x = 1, y = 1),
            intensity = 80
        )

    def animated_rain(self) -> None:
        self.rain.draw_update()
            



    
    
