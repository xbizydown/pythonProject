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


elbrus = House("Elbrus", 30)
elbrus.complex_info()
elbrus.go_to(5)
elbrus.go_to(31)

print("Length amount of floors in Elbrus:", len(elbrus))
print(str(elbrus))

#del elbrus