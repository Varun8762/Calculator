import tkinter as tk

def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)
        
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

def clear():
    display_var.set("0")

root = tk.Tk()
root.title("Calculator")
root.geometry("600x600")
root.configure(bg="black")
display_var = tk.StringVar()
display_var.set("0")
display = tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="aqua" , anchor="e", padx=10, pady=10)
display.grid(row=0, column=0, columnspan=4)

def demoColorChange(): buttons.configure(bg="red", fg="yellow")
buttons =[
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Agency FB", 18), bg="brown",command=lambda t=text: update_display(t))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", font=("Arial", 18), bg= "red" , command=clear)
clear_button.grid(row=5, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

calc_button = tk.Button(root, text="=", font=("Arial", 18), bg="green" , command=calculate)
calc_button.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
root.mainloop()
