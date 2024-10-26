import tkinter as tk
from common import window, mainentry
from calculator import plus, minus, multiply, divide
from gui import setup_gui

if __name__ == "__main__":
    setup_gui()

def create_buttons():
    plus_button = tk.Button(window, text='+', command=plus)
    plus_button.place(x=220, y=100, width=50, height=50)

    minus_button = tk.Button(window, text='-', command=minus)
    minus_button.place(x=220, y=160, width=50, height=50)

    multiply_button = tk.Button(window, text='*', command=multiply)
    multiply_button.place(x=280, y=160, width=50, height=50)

    divide_button = tk.Button(window, text='/', command=divide)
    divide_button.place(x=280, y=100, width=50, height=50)

if __name__ == "__main__":
    setup_gui()
    create_buttons()
    window.mainloop()