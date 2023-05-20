'''
from figure import Figure
square = Figure(width=5, length=10)
print(square.__str__())
'''
from triangle import Triangle
from rectangle import Rectangle
from calculate import CalculateArea
from commonclass import CommonClass
triangle = Triangle(10, 17)
rectangle = Rectangle(5, 10)
square = Rectangle(5)
area = CalculateArea()
print(f"Area of triangle {area.TriangleArea(triangle)}")
print(f"Area of rectangle {area.RectangleArea(rectangle)}")
print(f"Area of square {area.RectangleArea(square, True)}")
cClass = CommonClass()
cClass.ShowInfo(square)