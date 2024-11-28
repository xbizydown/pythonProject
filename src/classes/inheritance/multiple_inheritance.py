import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I am peaceful")
        else:
            print("Be careful, I am attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("I don't know how to speak")


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)  # Убрано _cords
        self.beak = True

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f"Here is the {eggs_count} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)  # Убрано _cords
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz * self.speed / 2  # Обновление координат


class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)  # Убрано _cords
        self._DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    def __init__(self, speed):
        super().__init__(speed)  # Убрано _cords
        self.sound = "Click-click-click"
        self.beak = True

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
print(db.get_cords())  # Добавлено print для отображения координат
db.dive_in(6)
print(db.get_cords())  # Добавлено print для отображения координат

db.lay_eggs()