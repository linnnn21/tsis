class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

shape = Shape()
square = Square(5)
rectangle = Rectangle(4, 6)

print("Area of shape:", shape.area())
print("Area of square:", square.area())
print("Area of rectangle:", rectangle.area())
