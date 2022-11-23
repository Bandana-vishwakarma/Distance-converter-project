import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x200")
root.resizable(False, False)
root.title("Distance Converter")

# Calculating the number of feet
metres_value = tk.StringVar()

# Updating our feet display label dynamically
feet_value = tk.StringVar(value="Feet shown here")


def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass


root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("segoe UI", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main,  textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, sticky="w")
metres_input.grid(column=1, row=0, sticky="ew")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="w")
feet_display.grid(column=1, row=1, sticky="ew")

calc_button.grid(column=0, row=2, columnspan=2, sticky="ew")

# winfo_children method
for child in main.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Shortcuts and keybindings
root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
