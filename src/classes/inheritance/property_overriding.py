class Vehicle:
    _COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white', 'yellow', 'pink']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

        if __color.lower() not in self._COLOR_VARIANTS:
            raise ValueError('Color is not in the list of available colors!')

    def get_model(self):
        return self.__model
    def get_horsepower(self):
        return self.__engine_power
    def get_color(self):
        return self.__color
    def set_color(self, new_color):
        if new_color.lower() not in self._COLOR_VARIANTS:
            raise ValueError('Color is not in the list of available colors!')
        self.__color = new_color

    def print_info(self):
        print(f'Owner: {self.owner}')
        print(f'Model: {self.__model}')
        print(f'Engine power: {self.__engine_power}')
        print(f'Color: {self.__color}')

class Sedan(Vehicle):
    def __init__(self, owner, __model, __color, __engine_power):
        super().__init__(owner, __model, __color, __engine_power)
        self.__PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
