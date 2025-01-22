# Условная конструкция. Операторы if, elif, else

def conditional_statements():
    name = input("What is your name? ")
    if name == "John":
        print("Hello John")
    else:
        print(f"Hello {name}")

conditional_statements()

# Fizz Buzz

def fizz_buzz():
    number = input("Type number to fizz buzz ")
    number = int(number)

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print("That number is not a Fizz or Buzz neither FizzBuzz\nYou only can use numbers that will divide to 3 or/and 5")

fizz_buzz()

    # Making same numbers detector

def conditional_statements_homework():
    first = input("Type the first number ")
    second = input("Type the second number ")
    third = input("Type the third number ")

    if first == second and second == third:
        print("All of the three numbers are the same!")
    elif first == second or second == third or first == third:
        print("There is only two same numbers!")
    elif first != second and second != third:
        print("None of the three numbers are the same!")

conditional_statements_homework()

