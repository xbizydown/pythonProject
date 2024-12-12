class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(color) == 3 and self.__is_valid_color(*color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]
            print('Invalid color')

        self.sides_count = len(sides)
        self.__sides = [0] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return True if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 else False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Invalid color')

    def __is_valid_side(self, side):
        return True if 0 < side < 100 else False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return len(self.__sides)

    def set_sides(self, *new_sides):
        for side in new_sides:
            if self.__is_valid_side(side):
                self.__sides.append(side)
            else:
                print('Invalid side')

        if len(self.__sides) != self.sides_count:
            print('Invalid number of sides')
        else:
            self.__sides = list(new_sides)

class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0]

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

class Cube(Figure):

    sides_count = 6

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
