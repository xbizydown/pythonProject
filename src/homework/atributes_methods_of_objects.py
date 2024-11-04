class House:

    def __init__(self, complex_name, floors):
        self.complex_name = complex_name
        self.floors = floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.floors:
            print("Invalid floor number!")
        else:
            for floor in range(1, new_floor + 1):
                print(f"You are now on the {floor} floor.")

    def complex_info(self):
        print(f"This is the {self.complex_name} complex.")

    # def __del__(self):
    #         print("The house has been destroyed.")

elbrus = House("Elbrus", 30)
elbrus.complex_info()
elbrus.go_to(5)
elbrus.go_to(31)

#del elbrus