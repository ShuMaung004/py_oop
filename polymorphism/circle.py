from shape import Shape

class Circle(Shape):
    def __init__(self,radius, color):
        super().__init__(color)
        self.__radius = radius    #encapsulation(private attribute)

    def area(self):
        return 3.14 * self.__radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.__radius