# program 52 :

# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def cal_area(self):
        return math.pi * (self.radius ** 2)

circle = Circle(5)
area = circle.cal_area()
print(f"The area of the circle: {area}")