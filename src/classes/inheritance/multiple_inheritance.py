# import random
#
# class Animal:
# 	live = True
# 	sound = None
# 	_DEGREE_OF_DANGER = 0
#
# 	def __init__(self, _cords, speed):
# 		self._cords = _cords
# 		self.speed = speed
#
# 	def move(self, dx, dy, dz):
# 		self._cords = (self._cords[0] + dx, self._cords[1] + dy, self._cords[2] + dz)
#
# 	def get_cords(self):
# 		print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
#
# 	def attack(self):
# 		if self._DEGREE_OF_DANGER < 5:
# 			print("Sorry, I am peaceful")
# 		elif self._DEGREE_OF_DANGER >= 5:
# 			print("Be careful, I am attacking you 0_0")
#
#
# class Bird(Animal):
# 	def __init__(self, _cords, speed):
# 		super().__init__(_cords, speed)
# 		self.beak = True
#
# 	def lay_eggs(self):
# 		eggs_count = random.randint(1, 4)
# 		print(f"Here is the {eggs_count} eggs for you")
#
#
# class AquaticAnimal(Animal):
# 	def __init__(self, _cords, speed):
# 		super().__init__(_cords, speed)
# 		self._DEGREE_OF_DANGER = 3
#
# 	def dive_in(self, dz):
# 		dz = abs(dz)
# 		self._cords = (self._cords[0], self._cords[1], self._cords[2] - dz * self.speed / 2)
#
#
# class PoisonousAnimal(Animal):
# 	def __init__(self, _cords, speed):
# 		super().__init__(_cords, speed)
# 		self._DEGREE_OF_DANGER = 8
#
#
# class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
# 	def __init__(self, speed):
# 		super().__init__((0, 0, 0), speed)
# 		self.sound = "Click-click-click"
# 		self.beak = True
#
# 	def speak(self):
# 		print(self.sound)
#
#
# db = Duckbill(10)
#
# print(db.live)
# print(db.beak)
#
# db.speak()
# db.attack()
#
# db.move(1, 2, 3)
# db.get_cords()
# db.dive_in(6)
# db.get_cords()
#
# db.lay_eggs()

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
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        return f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}"

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("I don't know how to speak")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
print(db.get_cords())
db.dive_in(6)
print(db.get_cords())

db.lay_eggs()