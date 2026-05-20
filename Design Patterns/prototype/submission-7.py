from abc import ABC, abstractmethod
from typing import List

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> "Rectangle":
        # Return a new Rectangle with the same dimensions
        return Rectangle(self.width, self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> "Square":
        # Return a new Square with the same side length
        return Square(self.length)

    def __repr__(self) -> str:
        return f"Square(length={self.length})"

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        return [shape.clone() for shape in shapes]