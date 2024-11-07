class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, complex_name: str, floors: int):
        self.complex_name = complex_name
        self.floors = floors


    def go_to(self, new_floor: int) -> None:
        if not 1 <= new_floor <= self.floors:
            print("\nInvalid floor number!")
            return
        for floor in range(1, new_floor + 1):
            print(f"\nYou are now on the {floor} floor.")

    def complex_info(self) -> None:
        print(f"\nThis is the {self.complex_name} complex, which contains {self.floors} floors.")

    def __len__(self) -> int:
        return self.floors

    def __del__(self):
            print(f"The {self.complex_name} has been destroyed. But it's history will be remembered.")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3

# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
# ex = Example('data', second=25, third=3.14)

    # def __str__(self):
    #     return f"Name: {self.complex_name}, Amount of floors: {self.floors}"
    #
    # def __lt__(self, other):
    #     return self.floors < other.floors
    #
    # def __eq__(self, other):
    #     return self.floors == other.floors
    #
    # def __gt__(self, other):
    #     return self.floors > other.floors
    #
    # def __le__(self, other):
    #     return self.floors <= other.floors
    #
    # def __ge__(self, other):
    #     return self.floors >= other.floors
    #
    # def __ne__(self, other):
    #     return self.floors != other.floors
    #
    # def __add__(self, value):
    #     if isinstance(value, House):
    #         return House(self.complex_name, self.floors + value.floors)
    #     elif isinstance(value, int):
    #         return House(self.complex_name, self.floors + value)
    #     else:
    #         raise TypeError("Unsupported type for addition")
    #
    # def __radd__(self, value):
    #     return self.__add__(value)
    #
    # def __iadd__(self, value):
    #     if isinstance(value, House):
    #         self.floors += value.floors
    #     elif isinstance(value, int):
    #         self.floors += value
    #     else:
    #         raise TypeError("Unsupported type for addition")
    #     return self

# elbrus = House("Elbrus", 40)
# elbrus.complex_info()
# elbrus.go_to(5)
# elbrus.go_to(41)
#
# print("Length amount of floors in Elbrus:", len(elbrus))
# del elbrus


#print(str(elbrus))
# moscow_city = House("Moscow City", 50)

# print("\n\n\n----------------------------------")
# print(elbrus)
# print(moscow_city)

# print("----------------------------------")

# print("Before addition:",elbrus == moscow_city, "(eq)")
# elbrus = elbrus + 10
# print(elbrus.floors, "(Elbrus add 10 floors)")
# print("After addition:",elbrus == moscow_city, "(eq)")
# print("----------------------------------")
# elbrus += 10
# print(elbrus.floors, "(Elbrus iadd 10 floors)")
# moscow_city = 10 + moscow_city
# print(moscow_city.floors, "(Moscow City radd 10 floors)")
# print("----------------------------------")
# print(elbrus > moscow_city, "gt")
# print(elbrus >= moscow_city, "ge")
# print(elbrus < moscow_city, "lt")
# print(elbrus <= moscow_city, "le")
# print(elbrus != moscow_city, "ne")
# print("----------------------------------")