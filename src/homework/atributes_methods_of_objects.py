class House:

    def __init__(self, complex_name, floors):
        self.complex_name = complex_name
        self.floors = floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("\nInvalid floor number!")
        else:
            for floor in range(1, new_floor + 1):
                print(f"\nYou are now on the {floor} floor.")

    def complex_info(self):
        print(f"\nThis is the {self.complex_name} complex. Which contains {self.floors} floors.")

    # def __del__(self):
    #         print("The house has been destroyed.")

    def __len__(self):
        return self.floors

    def __str__(self):
        return f"Name: {self.complex_name}, Amount of floors: {self.floors}"

    def __lt__(self, other):
        return self.floors < other.floors

    def __eq__(self, other):
        return self.floors == other.floors

    def __gt__(self, other):
        return self.floors > other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __ge__(self, other):
        return self.floors >= other.floors

    def __ne__(self, other):
        return self.floors != other.floors

    def __add__(self, value):
        if isinstance(value, House):
            return House(self.complex_name, self.floors + value.floors)
        elif isinstance(value, int):
            return House(self.complex_name, self.floors + value)
        else:
            raise TypeError("Unsupported type for addition")

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, House):
            self.floors += value.floors
        elif isinstance(value, int):
            self.floors += value
        else:
            raise TypeError("Unsupported type for addition")
        return self


elbrus = House("Elbrus", 40)
elbrus.complex_info()
elbrus.go_to(5)
elbrus.go_to(41)

print("Length amount of floors in Elbrus:", len(elbrus))
print(str(elbrus))

#del elbrus

moscow_city = House("Moscow City", 50)

print("\n\n\n----------------------------------")
print(elbrus)
print(moscow_city)

print("----------------------------------")

print("Before addition:",elbrus == moscow_city, "(eq)")
elbrus = elbrus + 10
print(elbrus.floors, "(Elbrus add 10 floors)")
print("After addition:",elbrus == moscow_city, "(eq)")
print("----------------------------------")
elbrus += 10
print(elbrus.floors, "(Elbrus iadd 10 floors)")
moscow_city = 10 + moscow_city
print(moscow_city.floors, "(Moscow City radd 10 floors)")
print("----------------------------------")
print(elbrus > moscow_city, "gt")
print(elbrus >= moscow_city, "ge")
print(elbrus < moscow_city, "lt")
print(elbrus <= moscow_city, "le")
print(elbrus != moscow_city, "ne")
print("----------------------------------")