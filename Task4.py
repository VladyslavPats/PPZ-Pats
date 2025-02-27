from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


radius = float(input("Введіть радіус кола: "))
circle = Circle(radius)
print(f"Площа кола: {circle.area():.2f}")

width = float(input("Введіть ширину прямокутника: "))
height = float(input("Введіть висоту прямокутника: "))
rectangle = Rectangle(width, height)
print(f"Площа прямокутника: {rectangle.area()}")
