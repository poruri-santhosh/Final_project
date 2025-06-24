import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    else:
        action = lambda x=text: press(x)
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
              command=action).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text='C', width=22, height=2, font=("Arial", 18),
          command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Run the app
root.mainloop()
