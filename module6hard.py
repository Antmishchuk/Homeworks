class Figure:
    __sides = []
    __color = []
    filled= False

    def __init__(self, rgb, *sides):
        self.color = list(rgb)
        self.sides = sides
        self.filled = True

    def get_color(self):


    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False
















