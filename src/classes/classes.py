class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
         print(f"Hello! Dear {self.name}, you are {self.age} years old.")

    def birthday(self):
        self.age += 1

human = Human("Sanjar", 21)

human.birthday()
human.say_info()