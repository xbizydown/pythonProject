import tkinter as tk
from common import window
from calculator import plus, minus, multiply, divide, equal, clear_entry, append_to_entry

def setup_gui():
    label = tk.Label(window, text='Enter Numbers and Get Results', font=('Helvetica', 15))
    label.place(x=20, y=0, width=300, height=40)

    button_width = 50
    button_height = 50
    button_font = ('Helvetica', 15)

    buttons = [
        ('1', 20, 100), ('2', 80, 100), ('3', 140, 100),
        ('4', 20, 160), ('5', 80, 160), ('6', 140, 160),
        ('7', 20, 220), ('8', 80, 220), ('9', 140, 220),
        ('0', 80, 280)
    ]

    for (text, x, y) in buttons:
        button = tk.Button(window, text=text, borderwidth=5, font=button_font,
                           command=lambda value=text: append_to_entry(value))
        button.place(x=x, y=y, width=button_width, height=button_height)


    plus_button = tk.Button(window, text='+', borderwidth=5, font=button_font, command=plus)
    plus_button.place(x=220, y=100, width=50, height=50)


    minus_button = tk.Button(window, text='-', borderwidth=5, font=button_font, command=minus)
    minus_button.place(x=220, y=160, width=50, height=50)

    divide_button = tk.Button(window, text='/', borderwidth=5, font=button_font, command=divide)
    divide_button.place(x=280, y=100, width=50, height=50)

    multiply_button = tk.Button(window, text='*', borderwidth=5, font=button_font, command=multiply)
    multiply_button.place(x=280, y=160, width=50, height=50)


    equal_button = tk.Button(window, text='=', borderwidth=5, font=button_font, command=equal)
    equal_button.place(x=220, y=220, width=110, height=50)
    clean = tk.Button(window, text='C', borderwidth=5, font=button_font, command=clear_entry)
    clean.place(x=220, y=280, width=110, height=50)

    window.mainloop()
    window.quit()