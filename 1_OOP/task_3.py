import math


class Shape:

    def area(self):
        return 0

    def perimeter(self):
        return 0

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi ** self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())

circle = Circle(4)
print(circle.area())
print(circle.perimeter())

