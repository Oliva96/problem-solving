
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.color = 'Green'

    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def area(self):
        return 3.14 * (self.__radius ** 2)
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        self.color = 'Blue'

    def area(self):
        return (self.base * self.height) / 2


t = Triangle(2, 4)
print(t.color)

# r = Rectangle(10, 20)
# print(r.color)

shapes = [Rectangle(10, 20), Triangle(10, 2)]
for shape in shapes:
    print(f'this is a shape with area: {shape.area()} and color: {shape.color}')

# Fixed-size sliding window (last 3 items)