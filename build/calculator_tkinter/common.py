import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)

mainentry = tk.Entry(window, width=27, borderwidth=5, font=('Helvetica', 15))
mainentry.place(x=20, y=50)
mainentry.focus_set()