
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x480")
root.resizable(False, False)
root.configure(bg="#222222")

# Display
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 25),
    bg="#333333",
    fg="white",
    bd=0,
    justify="right"
)

display.pack(fill="both", padx=15, pady=20, ipady=15)


# Button functions
def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Create buttons
for row in buttons:

    frame = tk.Frame(root, bg="#222222")
    frame.pack(expand=True, fill="both", padx=10)

    for button in row:

        if button == "=":
            command = calculate
            color = "#e67e22"

        else:
            command = lambda x=button: click(x)
            color = "#444444"

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            activebackground="#666666",
            bd=0,
            command=command
        ).pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )


# Clear button
tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16, "bold"),
    bg="#c0392b",
    fg="white",
    bd=0,
    command=clear
).pack(fill="both", padx=14, pady=12, ipady=8)


# Run application
root.mainloop()
