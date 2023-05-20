from rectangle import Rectangle
from calculate import CalculateArea
class CommonClass(Rectangle, CalculateArea):
    def ShowInfo(self, rectangle = Rectangle()):
        print(super().RectangleArea(rectangle, True))