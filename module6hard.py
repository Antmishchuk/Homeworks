
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













circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())









