import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def print_info(self):
        print("Circle Information:")
        print(f" - Radius: {self.radius}")
        print(f" - Area: {self.area():.2f}")
        print(f" - Perimeter: {self.perimeter():.2f}")

custom_radius = float(input("Enter the radius of the circle: "))
custom_circle = Circle(custom_radius)
custom_circle.print_info()