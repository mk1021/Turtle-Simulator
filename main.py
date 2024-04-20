import tkinter as tk
from tkinter import colorchooser

## INITIALISATION

window = tk.Tk()

coords = [150, 150]

canvas = tk.Canvas(window, bg="white", height=300, width=300)
canvas.grid(column=0, row=0, columnspan=4)

# SPEC: Turtle should be able to change line colour
current_line_color = "black"

# SPEC: Turtle should be able to move without drawing a line - use a toggle for pen drawing
pen_draw = True


## MOVEMENT CONTROLS

# Move Up
def move_up():
    canvas.create_line(coords[0], coords[1], coords[0], coords[1] + 10, fill=current_line_color, width=1)
    coords[1] += 10

# Move Down
def move_down():
    canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 10, fill=current_line_color, width=1)
    coords[1] -= 10

# Move Left
def move_left():
    canvas.create_line(coords[0], coords[1], coords[0] - 10, coords[1], fill=current_line_color, width=1)
    coords[0] -= 10

# Move Right
def move_right():
    canvas.create_line(coords[0], coords[1], coords[0] + 10, coords[1], fill=current_line_color, width=1)
    coords[0] += 10

# Turn Left
def turn_left():
    # press the button followed by a number which is equal to the number of degrees it turns
    pass

# Turn Right
def turn_right():
    # press the button followed by a number which is equal to the number of degrees it turns
    pass


## LINE COLOR 

# Change Line Color
def change_line_color():
    global current_line_color

    chosen_color = colorchooser.askcolor(title="Choose color")
    print(chosen_color)

    current_line_color = chosen_color[1]


## PEN UP/DOWN

# Toggle Pen
def toggle_pen():
    global pen_draw
    pen_draw = not pen_draw


## BUTTONS

# Movement Controls
tk.Button(window, text="↑", command=move_up).grid(column=0, row=1)
tk.Button(window, text="↓", command=move_down).grid(column=1, row=1)
tk.Button(window, text="←", command=move_left).grid(column=2, row=1)
tk.Button(window, text="→", command=move_right).grid(column=3, row=1)
tk.Button(window, text="↰", command=turn_left).grid(column=1, row=2)
tk.Button(window, text="↱", command=turn_left).grid(column=2, row=2)

# Change Color
tk.Button(window, text="Change Color", command=change_line_color).grid(column=2, row=3)

# Pen Up/Down
tk.Button(window, text="Pen Up/Down", command=toggle_pen).grid(column=1, row=3)


window.mainloop()
