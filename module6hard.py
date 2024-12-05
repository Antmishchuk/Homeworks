class Figure:
    sides_count = 0


    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color


    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False
















