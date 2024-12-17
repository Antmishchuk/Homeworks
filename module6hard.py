from math import sqrt
class Figure:
    sides_count = 0


    def __init__(self, color, *sides, filled = False):
        self.__color = color
        self.__sides = sides
        self.filled = filled

    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
                and isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)





    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not isinstance(side, int) or side < 0:
                    return False
            else:
                return True
        else:
            return False


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum( self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) and len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            pass
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = len(self.__sides) / 2*3.14


    def get_square(self):
        s = self.__radius**2*3.14
        return s

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides


    def get_square(self):
        p = (self.__sides[0] + self.__sides[1] + self.__sides[2]) / 2
        s = sqrt(p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2]))
        return s


class Cube(Figure):
    sides_count = 12
    def init(self, color, *sides):
        if len(sides) == 1:
            self.__sides = [sides[0]] * 12
        else:
            self.__sides =[1] * sides_count
        super().init(color, *sides)












# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6, 9)
print(cube1.get_sides())
# triangle1 = Triangle((200, 200, 100), 3, 4, 5)
# print(triangle1.get_square())

# Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())

# Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())


















