from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,color):
        self.__color = color #encapsulation (private attribute)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def get_color(self): #getter method for encapsulation
        return self.__color
    
    def set_color(self,color): #setter method for encapsulation
        self.__color = color