class Figure:
    def __init__(self):
        self.__sides = []
        self.__color = [0, 0, 0]
        self.filled = False
        sides_count = 0

    def get_color(self):
        return self.__color
    def __is_valid_color(self):
        if any(c < 0 or c > 255 for c in self.__color):
            raise ValueError("Color should be within RGB range!")

    def set_color(self, 0, 0, 0):


    def __is_valid_sides(self):
        pass

    def get_sides(self):
        return self.__sides
    def __len__(self):
        pass
    def set_sides(self):
        pass

class Circle(Figure):
    pass

class Triangle(Figure):
    pass

class Cube(Figure):
    pass