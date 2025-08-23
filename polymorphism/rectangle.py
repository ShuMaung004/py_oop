from shape import Shape

class Rectangle(Shape):
    def __init__(self,width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)
