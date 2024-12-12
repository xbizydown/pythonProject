class Figure:
    def __init__(self, color, *sides):
        self._color = color
        self._sides = list(sides)
        self.filled = False
        self.sides_count = 0

    def get_color(self):
        return self._color

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(x, int) and x > 0 for x in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 1
        if len(sides) != self.sides_count:
            self._sides = [1]
        self._radius = self._sides[0]

    def get_square(self):
        return 3.14 * (self._radius ** 2)


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 3
        if len(sides) != self.sides_count:
            self._sides = [1] * self.sides_count

    def get_square(self):
        a, b, c = self._sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 12
        if len(sides) != 1:
            self._sides = [1] * self.sides_count
        else:
            self._sides = [sides[0]] * self.sides_count

    def get_volume(self):
        return self._sides[0] ** 3