import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("0", 3, 0),
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=40, pady=20,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row+1, column=column)

button_clear = tk.Button(root, text="Clear", padx=79, pady=20,
                         command=button_clear)
button_clear.grid(row=4, column=0, columnspan=2)

button_equal = tk.Button(root, text="=", padx=89, pady=20,
                         command=button_equal)
button_equal.grid(row=4, column=2)

root.mainloop()