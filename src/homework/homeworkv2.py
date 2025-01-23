# conditional statement. operators if, elif, else

def conditional_statements():
    name = input("What is your name? ")
    if name == "John":
        print("Hello John")
    else:
        print(f"Hello {name}")

# commented call of function
# conditional_statements()

    # fizz fuzz

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

# commented call of function
# fizz_buzz()

    # making same numbers detector

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

# commented call of function
# conditional_statements_homework()

    # loop while
def loop_while():
    while True:
        number = int(input(f"Type the number: "))
        if number % 2 == 0:
            print("Even number")
            break
        else:
            print("Odd number")
            break

# commented call of function
# loop_while()

    # loop while homework

def loop_while_homework():
    numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    index = 0
    while index < len(numbers):
        if numbers[index] == 0:
            index += 1
            continue
        if numbers[index] < 0:
            break
        elif numbers[index] > 0:
            print(numbers[index])
            index += 1

# commented call of function
# loop_while_homework()

def loop_for():
    result = list()
    for i in range(1, 10):
        for j in range(1, 10):
            result.append(i * j)
            print(result)

# commented call of function
# loop_for()

def primes_homework():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    primes = []
    not_primes = []

    for number in numbers:
        if number == 1:
            continue

        for i in range(2, number):
            if number % i == 0:
                not_primes.append(i)
                break
            else:
                primes.append(i)
                break

    print(primes)
    print(not_primes)

# commented call of function
primes_homework()