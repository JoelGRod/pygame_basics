from pygame import Surface

from context.examples.main.basics.domain.rect import Rectangle

from context.examples.main.shared.aggregates import (Position, Dimensions, Color)

class Shapes:
    def __init__(self, screen: Surface, color: tuple[int, ...]) -> None:
        self.screen = screen
        self.color = Color(color)

    def create_rectangle(self) -> None:
        rectangle = Rectangle(
            self.screen, 
            Position(x=300, y=100), 
            Dimensions(width=200, height=150, weight=5), 
            self.color)
        rectangle.draw()

    def create_rectangles(self) -> None:
        rectangle = Rectangle(
            self.screen, 
            Position(x=100, y=500), 
            Dimensions(width=50, height=100, weight=5), 
            self.color)
        rectangle.draw_rects(step = 100)