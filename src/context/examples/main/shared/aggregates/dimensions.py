# Value Object

class Dimensions:
    def __init__(self, width: float, height: float, weight: float = 1) -> None:
        self.width = width
        self.height = height
        self.weight = weight