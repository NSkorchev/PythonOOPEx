from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        ...


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.height * self.base / 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.pi = Circle.PI

    def calculate_area(self):
        return self.pi * self.radius * self.radius


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Circle(2, 3.14), Rectangle(2, 3), Rectangle(1, 6), Triangle(3, 2)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
