import tkinter as tk
from tkinter import colorchooser
from tkinter import *

## INITIALISATION

window = tk.Tk()

coords = [150, 150]

canvas = tk.Canvas(window, bg="white", height=300, width=300)
canvas.grid(column=0, row=0, columnspan=4)

# SPEC: Turtle should be able to change line colour
current_line_color = "black"

# Change Line Width
current_line_width = 0

# SPEC: Turtle should be able to move without drawing a line - use a toggle for pen drawing
pen_state = tk.IntVar()
pen_state.set(1) # true

# Command List
go_flag = False
list_of_commands = []

# Storing Sequences
sequence_list = []


## CURSROR

# Initialise Cursor
cursor_size = 4
cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")

# Move Cursor
def update_cursor():
    canvas.coords(cursor, coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size)


## LINE COLOR & THICKNESS

# Change Line Color
def change_line_color():
    global current_line_color

    chosen_color = colorchooser.askcolor(title="Choose color")
    # print(chosen_color)

    current_line_color = chosen_color[1]

def change_line_width(val):
    global current_line_width
    current_line_width = val


## PEN UP/DOWN

# Toggle Pen
def toggle_pen_state():
    global pen_state
    
    # store_command(toggle_pen_state)
    if go_flag:
        pen_state.set(1 - pen_state.get())


## MOVEMENT CONTROLS

# Move Up
def move_up():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0], coords[1] + 10, fill=current_line_color, width=current_line_width)
        coords[1] += 10
        # update_cursor()
        

# Move Down
def move_down():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 10, fill=current_line_color, width=current_line_width)
        coords[1] -= 10
        # update_cursor()

    
    

# Move Left
def move_left():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0] - 10, coords[1], fill=current_line_color, width=current_line_width)
        coords[0] -= 10
        # update_cursor()

    


# Move Right
def move_right():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0] + 10, coords[1], fill=current_line_color, width=current_line_width)
        coords[0] += 10
        # update_cursor()




# Get Angle for Rotation
def get_angle(var):
    pass

# Turn Left
def turn_left(angle):
    # press the button followed by a number which is equal to the number of degrees it turns
    
    pass

# Turn Right
def turn_right(angle):
    # press the button followed by a number which is equal to the number of degrees it turns
    pass



## SEQUENCING AND LOOPS

# Sequences
def set_sequence():
    global sequence_list
    
    # append every button pressed into list

    pass

# Loops
def repeat():
    global cursor

    canvas.delete("all")
    cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")
    go()


## STORING COMMANDS

def store_command(command):
    list_of_commands.append(command)
    print('Storing command:', command)


## GO 

def go():
    global go_flag
    go_flag = True

    print('now in go function')

    for command in list_of_commands:
        command()
        update_cursor()  
        window.update_idletasks()
        window.after(500)

    print(list_of_commands)
    # list_of_commands.clear()


## CLEAR MEMORY

def clear_memory():
    global coords
    global cursor

    coords = [150, 150]
    canvas.delete("all") 
    cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")
    list_of_commands.clear()
    print('clear memory')

    
## BUTTONS

# Movement Controls
tk.Button(window, text="↑", command=lambda: store_command(move_up)).grid(column=0, row=1)
tk.Button(window, text="↓", command=lambda: store_command(move_down)).grid(column=1, row=1)
tk.Button(window, text="←", command=lambda: store_command(move_left)).grid(column=2, row=1)
tk.Button(window, text="→", command=lambda: store_command(move_right)).grid(column=3, row=1)
tk.Button(window, text="↰", command=lambda: store_command(turn_right)).grid(column=1, row=2)
tk.Button(window, text="↱", command=lambda: store_command(turn_left)).grid(column=2, row=2)

# Change Color
tk.Button(window, text="Change Color", command=lambda: store_command(change_line_color)).grid(column=0, row=3)

# Pen Up/Down
# tk.Button(window, text="Pen Up/Down", command=toggle_pen).grid(column=1, row=3)
tk.Checkbutton(window, onvalue=1, offvalue=0, height=2, width=10, text="Pen Up", command=lambda: store_command(toggle_pen_state)).grid(column=1, row=3)

# Choose Angle Input

# Line Thickness Slider
w = tk.DoubleVar()
line_width = tk.Scale(window, variable=w, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Width", command=lambda: store_command(change_line_width)).grid(column=0, row=4, columnspan=2)

# Sequences & Loops
tk.Button(window, text="[ Sequence ]", command=set_sequence).grid(column=0, row=5)
tk.Button(window, text="Repeat", command=repeat).grid(column=1, row=5)

# Go & clear_memory
tk.Button(window, text="GO", command=go, bg="green").grid(column=2, row=6)
tk.Button(window, text="CM", command=clear_memory, bg="red").grid(column=0, row=6)

window.mainloop()
