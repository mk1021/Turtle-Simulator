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


## CURSROR

# Initialise Cursor
cursor_size = 4
cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")

# Move Cursor
def update_cursor():
    canvas.coords(cursor, coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size)


## MOVEMENT CONTROLS

# Move Up
def move_up():
    if pen_draw:
        canvas.create_line(coords[0], coords[1], coords[0], coords[1] + 10, fill=current_line_color, width=1)
    coords[1] += 10
    update_cursor()

# Move Down
def move_down():
    if pen_draw:
        canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 10, fill=current_line_color, width=1)
    coords[1] -= 10
    update_cursor()

# Move Left
def move_left():
    if pen_draw:
        canvas.create_line(coords[0], coords[1], coords[0] - 10, coords[1], fill=current_line_color, width=1)
    coords[0] -= 10
    update_cursor()

# Move Right
def move_right():
    if pen_draw:
        canvas.create_line(coords[0], coords[1], coords[0] + 10, coords[1], fill=current_line_color, width=1)
    coords[0] += 10
    update_cursor()

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
