# name = "Sanjar"
# print(f"Name: {name}")
# age = 20
# print(f"Age: {age}")
# age = age + 1
# print(f"Age: {age}")
# is_student = True
# print(f"Is Student: {is_student}")
#
# my_string = input("Enter a string: ")
# print(f"Amount of Symbols:", str(len(my_string)))
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.replace(" ", ""))
# print(my_string[0])
# print(my_string[-1])
#
# immutable_var = (["Benedict", 33, "aboba", 8.8005553535], 123, 4444)
# immutable_var[0] [0] = "nigga"
# print(immutable_var)
# mutable_list = ["Benedict", 33, "aboba", 8.8005553535]
# mutable_list.append('it ain't my fault she calls me all the time when been on the grind')
# print(mutable_list)
#
# phone_book = {'George': 8800553535, 'Steve': 500}
# phone_book.update({'ALex:': 1488,
#                    'Biz': 8888})
# print(phone_book.keys(), phone_book.values(), phone_book.items(), phone_book.get('Steve'))
# get_number = phone_book.pop('George')
# print(phone_book)
# print(get_number)
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(numbers) #You can't call them from ID or something
#
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
#
# a = 1+2j
# print(a, "is complex number?", isinstance(1+2j, complex))
#
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Nigga', 'Aaron'}
# students = sorted(students)
# average_grade = {}#
# for i in range(len(grades)):
# 	average_grade[students[i]] = sum(grades[i]) / len(grades[i])
# print(average_grade)
#
# if (name := input("Enter your name: ").lower()) in [n.lower() for n in ["womp-womp", "aboba", "huevo"]]:
# 	print(f"Hello {name}!")
# else:
# 	print(f"I don't know you {name}!")
#
# number = int(input("Enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
# 	print('FizzBuzz')
# elif number % 5 == 0:
# 	print('Buzz')
# elif number % 3 == 0:
# 	print('Fizz')
# else: print(f"The number {number} is either not Fizz or Buzz or FizzBuzz.")
#
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
#
# while 1 > 0:
# 	number = int(input("Enter a number: "))
# 	if 2 != 0:
# 		print(number, "is an odd number.")
# 		break
# 	else:
# 		print(number, "is an even number.")
# 		continue
#
#
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# my_list_index = 0
# while my_list_index < len(my_list):
# 	if my_list[my_list_index] in [42, 69, 322, 13, 99]:
# 		print(my_list[my_list_index])
# 	my_list_index += 1
#
#
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# i = 0
# while i <= len(my_list):
#     if my_list[i] < 0:
#         break
#     elif my_list[i] > 0:
#         print(my_list[i])
#     i += 1
#
# def display_invoice(username, amount, due_date):
# 	print(f"Hello {username}!")
# 	print(f"Your bill of ${amount:.2f} is {due_date}")
#
# display_invoice("xBizyDown", 42.50, "01/01")
#
# def add(x, y):
# 	z = x + y
# 	return z
#
# def subtract(x, y):
# 	return x - y
#
# def multiply(x, y):
# 	return x * y
#
# def divide(x, y):
# 	return x / y
#
# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(2, 2))
#
# number = 3.14159
# integer = 42
# string = "Hello"
#
# print("{:.2f}".format(number))  # 3.14
# print("{:d}".format(integer))    # 42
# print("{:.2e}".format(number))    # 3.14e+00
# print("{:s}".format(string))      # Hello
# print("{:.2%}".format(0.1234))   # 12.34%
# print("{:<10}".format(string))    # Hello
# print("{:>10}".format(string))    #      Hello
# print("{:^10}".format(string))     #   Hello
# print("{:05d}".format(integer))    # 00042
#
# def create_name(first, last):
# 	first = first.capitalize()
# 	last = last.capitalize()
# 	return first, last
#
# full_name = input(f"Type your First and Last name: ")
# first_name, last_name = full_name.split()
# formatted_name = create_name(first_name, last_name)
#
# print(f"Hello! {formatted_name}")
#
# def get_matrix(n, m, value):
# 	matrix = []
# 	for i in range(n):
# 		n = []
# 		for j in range(m):
# 			n.append(value)
# 		matrix.append(n)
# 	return matrix
#
# result1 = get_matrix(2, 2, 10)
# result2 = get_matrix(3, 5, 42)
# result3 = get_matrix(4, 2, 13)
#
# print(result1)
# print(result2)
# print(result3)
#
# #1st program
# print(9 ** 0.5)
#
# #2nd program
# print(9.99 > 9.98 and 1000 != 1000.1)
#
# #3rd program
# result1 = 2 * 2 +2
# result2 = 2 * (2 + 2)
# comparison = result1 == result2
# print(f"{result1}\n{result2}\n{comparison}")
#
# #4th program
# float_number = "123.456"
# print(type(float(float_number)), float_number)
# float_number = float(float_number)
# float_shift = float_number * 10
# print(float_shift)

# number = int(input("Enter a number from 3 to 20: "))
# password = ""
# for i in range(1, 21):
# 	for j in range(i + 1, 21):
# 		if i != j and i != number and j != number:
# 			sum_pair = i + j
# 			if number % sum_pair == 0:
# 				number_pair = f"{i}{j}"
# 				password += number_pair
# 				break
# print(password)

# calls = 0
# def count_calls():
# 	global calls
# 	calls += 1
# 	return
#
# def string_info(string):
# 	count_calls()
# 	length = len(string)
# 	upper_string = string.upper()
# 	lower_string = string.lower()
# 	return length, upper_string, lower_string
#
# def is_contains(string, list_of_strings):
# 	count_calls()
# 	lower_string = string.lower()
# 	for item in list_of_strings:
# 		if lower_string == item.lower():
# 			return True
# 	return False
#
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)

# def func_with_params(a, b=2, c=None):
#     if c is None:
#         c = []
#         c.append(a)
#     print(c)
#
#
#
# func_with_params(3)
# func_with_params(4)
# func_with_params(5)
# func_with_params(6)

# domain = (".net", ".ru", ".com")
# at = "@"
# def send_email(message, recipient, *, sender = "university.help@gmail.com"):
#
# 	if (at not in recipient or not recipient.endswith(domain)) or (at not in sender or not sender.endswith(domain)):
# 		print(f"Alert!\nE-mail address should contain @ or .net/.ru/.com or .com.!\n")
#
# 	elif sender == recipient:
# 		print(f"Alert!\nYou can't send messages from {sender} to {recipient}!\n")
#
# 	elif sender == "university.help@gmail.com":
# 		print(f"Success!\nYour message has been successfully sent! From {sender} to {recipient}!\n")
#
# 	elif sender != "university.help@gmail.com":
# 		print(f"Alert!\nNON-STANDART SENDER! Your message has been sent from {sender} to {recipient}!\n")
#
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# def print_params(a = 1, b = "string", c = True):
# 	print(a, b, c)
#
# print_params()
# print_params(10)
# print_params(b = 25)
# print_params(c = [1, 2, 3])
#
# values_list = ["bumboclaat", 8888.88, False]
# values_list2 = [True, "False"]
# values_dict = {"a": 999, "b": 12.21, "c": "oaoaoa"}
#
# print_params(*values_list)
# print_params(*values_list2, 42)
# print_params(**values_dict)

def single_root_words(root_word, *others):
	same_words = []
	root_word = root_word.lower()
	for other in others:
		if root_word in other.lower() or other.lower() in root_word.lower():
			same_words.append(other)
	return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
