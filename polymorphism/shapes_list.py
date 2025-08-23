from shape import Shape
from circle import Circle
from rectangle import Rectangle

shapes:Shape = [
    Circle(5, "red"),
    Rectangle(4,6,"Blue")
]

for shape in shapes:
    print(f"Shape : {shape.__class__.__name__}, Color : {shape.get_color()}")