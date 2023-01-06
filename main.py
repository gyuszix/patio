# class Rectangle:
#     def __init__(self,length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def parameter(self):
#         return self.length * 2 + self.width * 2
#
#
# class Square:
#     def __init__(self, length):
#         self.length = length
#
#     def area(self):
#         return self.length ** 2
#
#     def parameter(self):
#         return self.length * 4
#
#
# first_rectangle = Rectangle(5,4)
# first_square = Square(5)
#
# print(first_rectangle.parameter())
# print(first_rectangle.area())
#
# print(first_square.parameter())
# print(first_square.area())

#so it seems that doing it this way as seen above is redundant because when it doesn't actually represent the
#relationship between the two shapes. A better way of writing this would be just to inherit and use the super method

class Rectangle:
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * self.length

    def volume(self):
        face_area = super().area()
        return  face_area * self.length


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri
