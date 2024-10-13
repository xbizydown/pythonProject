# import tkinter as tk
# from common import mainentry
#
# def append_to_entry(value):
#     current_text = mainentry.get()
#     new_text = current_text + str(value)
#     mainentry.delete(0, tk.END)
#     mainentry.insert(0, new_text)
#
# def plus():
#     expression = mainentry.get()
#     try:
#         parts = expression.split("+")
#         first_number = float(parts[0])
#         second_number = float(parts[1])
#         result = first_number + second_number
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, result)
#
#     except Exception as e:
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, "Error")
#
# def minus():
#     expression = mainentry.get()
#     try:
#         parts = expression.split("-")
#         first_number = float(parts[0])
#         second_number = float(parts[1])
#         result = first_number - second_number
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, result)
#
#     except Exception as e:
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, "Error")
#
# def multiply():
#     expression = mainentry.get()
#     try:
#         parts = expression.split("*")
#         first_number = float(parts[0])
#         second_number = float(parts[1])
#         result = first_number * second_number
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, result)
#
#     except Exception as e:
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, "Error")
#
# def divide():
#     expression = mainentry.get()
#     try:
#         parts = expression.split("/")
#         first_number = float(parts[0])
#         second_number = float(parts[1])
#         result = first_number / second_number
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, result)
#
#     except Exception as e:
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, "Error")
#
# def equal():
#     expression = mainentry.get()
#     try:
#         if not all(c in "0123456789+-*/. " for c in expression):
#             raise ValueError("Invalid input")
#
#         result = eval(expression)
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, result)
#     except Exception as e:
#         mainentry.delete(0, tk.END)
#         mainentry.insert(0, "Error")
#
# def clear_entry():
#     mainentry.delete(0, tk.END)

import tkinter as tk
from common import mainentry

current_value = ""
operation = None
first_number = None

def append_to_entry(value):
    current_text = mainentry.get()
    new_text = current_text + str(value)
    mainentry.delete(0, tk.END)
    mainentry.insert(0, new_text)

def set_operation(op):
    global first_number, operation, current_value
    first_number = int(mainentry.get())
    operation = op
    current_value = ""
    mainentry.delete(0, tk.END)

def plus():
    set_operation('plus')

def minus():
    set_operation('minus')

def multiply():
    set_operation('multiply')

def divide():
    set_operation('divide')

def equal():
    global current_value, first_number, operation
    try:
        second_number = int(mainentry.get())
        if operation == 'plus':
            result = first_number + second_number
        elif operation == 'minus':
            result = first_number - second_number
        elif operation == 'multiply':
            result = first_number * second_number
        elif operation == 'divide':
            if second_number != 0:
                result = first_number / second_number
            else:
                raise ValueError("Cannot divide by zero")
        else:
            raise ValueError("Invalid operation")

        mainentry.delete(0, tk.END)
        mainentry.insert(0, result)
    except Exception as e:
        mainentry.delete(0, tk.END)
        mainentry.insert(0, "Error")

def clear_entry():
    global current_value, first_number, operation
    current_value = ""
    first_number = None
    operation = None
    mainentry.delete(0, tk.END)