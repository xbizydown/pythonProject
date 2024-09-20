# name = "Sanjar"
# print(f"Name: {name}")
# age = 20
# print(f"Age: {age}")
# age = age + 1
# print(f"Age: {age}")
# is_student = True
# print(f"Is Student: {is_student}")

# my_string = input("Enter a string: ")
# print(f"Amount of Symbols:", str(len(my_string)))
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(" ", ""))
# print(my_string[0])
# print(my_string[-1])

# immutable_var = (["Benedict", 33, "aboba", 8.8005553535], 123, 4444)
# immutable_var[0] [0] = "nigga"
# print(immutable_var)
# mutable_list = ["Benedict", 33, "aboba", 8.8005553535]
# mutable_list.append('it ain't my fault she calls me all the time when been on the grind')
# print(mutable_list)

# phone_book = {'George': 8800553535, 'Steve': 500}
# phone_book.update({'ALex:': 1488,
#                    'Biz': 8888})
# print(phone_book.keys(), phone_book.values(), phone_book.items(), phone_book.get('Steve'))
# get_number = phone_book.pop('George')
# print(phone_book)
# print(get_number)
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(numbers) #You can't call them from ID or something

# my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
# print("Dict:", my_dict)
# print("Existing value:", my_dict.get('Masha'))
# print("Not existing value:", my_dict.get('Somebody'))
# print("Deleted value:", my_dict.pop('Egor'))
# my_dict.update({'Slava': 1985,
#                 'Alexandr': 1995})
# print("Modified dictionary:", my_dict)
#
# my_set = {1, 'Apple', 42.314}
# print(f"\nSet:", my_set)
# my_set.discard(1)
# my_elements = [13, (5, 6, 1.6)]
# my_set.update(my_elements)
# print("Modified set:", my_set)

# a = 1+2j
# print(a, "is complex number?", isinstance(1+2j, complex))

# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Nigga', 'Aaron'}
# students = sorted(students)
# average_grade = {}#
# for i in range(len(grades)):
# 	average_grade[students[i]] = sum(grades[i]) / len(grades[i])
# print(average_grade)

# if (name := input("Enter your name: ").lower()) in [n.lower() for n in ["womp-womp", "aboba", "huevo"]]:
# 	print(f"Hello {name}!")
# else:
# 	print(f"I don't know you {name}!")

# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
# 	print('FizzBuzz')
# elif number % 5 == 0:
# 	print('Buzz')
# elif number % 3 == 0:
# 	print('Fizz')
# else: print(f"The number {number} is either not Fizz or Buzz or FizzBuzz.")

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# third = int(input("Enter third number: "))
#
# if first == second == third:
# 	print(f"All numbers are same!\n{first}, {second}, {third}")
# elif first != second and second != third and third != first:
# 	print(f"Womp-Womp there is no same numbers!\n{first}, {second}, {third}")
# elif first == second or first == third or third == second:
# 	print(f"Only two numbers are same!\n{first}, {second}, {third}")

# while 1 > 0:
# 	number = int(input("Enter a number: "))
# 	if 2 != 0:
# 		print(number, "is an odd number.")
# 		break
# 	else:
# 		print(number, "is an even number.")
# 		continue


# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# my_list_index = 0
# while my_list_index < len(my_list):
# 	if my_list[my_list_index] in [42, 69, 322, 13, 99]:
# 		print(my_list[my_list_index])
# 	my_list_index += 1


# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# i = 0
# while i <= len(my_list):
#     if my_list[i] < 0:
#         break
#     elif my_list[i] > 0:
#         print(my_list[i])
#     i += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
	if number == 1:
		continue

	is_prime = True
	for i in range(2, number):
		if number % i == 0:
			is_prime = False
			break

	if is_prime:
		primes.append(number)
	else:
		not_primes.append(number)

print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
