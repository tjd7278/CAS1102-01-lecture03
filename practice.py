import math
from abc import abstractmethod
from typing import List


class Shape(abc):
    # TODO: Define the method "measure".
    """
    - This is an abstract method, so it should just raise NotImplementedError.
    """

    @abstractmethod
    def measure(self):
        pass


# TODO: Create a Circle class that inherits from Shape.
# - Initialize it with a radius (float).
# - Implement the measure method to return the area of the circle.
class Circle(Shape):
    def __init__(self,radius):
        self.r = float(radius)
    def measure(self):
        self.A = (self.r**2)*(math.pi)
        return self.A


# TODO: Create a Rectangle class that inherits from Shape.
# - Initialize it with width and height (floats).
# - Implement the measure method to return the area of the rectangle.
class Rectangle(Shape):
    def __init__(self,width,height):
        self.w = float(width)
        self.h = float(height)
    def measure(self):
        self.A = self.w * self.h
        return self.A


# TODO: Create a Triangle class that inherits from Shape.
# - Initialize it with three vertices, each a tuple of (x, y).
# - Implement the measure method to return the area of the triangle using Heron's formula.
class Triangle(Shape):
    def __init__(self,p1,p2,p3):
        self.a = float(( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )**(1/2))
        self.b = float(( (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2 )**(1/2))
        self.c = float(( (p3[0]-p1[0])**2 + (p3[1]-p1[1])**2 )**(1/2))
        self.s = (self.a + self.b + self.c)/2
    def measure(self):
        self.A = self.s*((self.s-self.a)*(self.s-self.b)*(self.s-self.c))**(1/2)
        return self.A

if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(radius=1.0),
        Rectangle(width=2.0, height=5.0),
        Triangle(p1=(0, 0), p2=(3, 0), p3=(0, 4)),
    ]

    print("Individual areas:", [round(s.measure(), 4) for s in shapes])
