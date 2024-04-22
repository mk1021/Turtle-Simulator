import tkinter as tk
from tkinter import colorchooser
from tkinter import *
import math

## INITIALISATION

window = tk.Tk()

coords = [150, 150]

canvas = tk.Canvas(window, bg="white", height=300, width=300)
canvas.grid(column=0, row=0, columnspan=4)

# SPEC: Turtle should be able to change line colour
current_line_color = "black"

# Change Line Width
current_line_width = 1

# SPEC: Turtle should be able to move without drawing a line - use a toggle for pen drawing
pen_state = tk.IntVar()
pen_state.set(1) # true

# Command List
go_flag = False
list_of_commands = []

# Storing Sequences
sequence_list = []

# Current Orientation (0: right, 90: up, 180: left, 270: down)
current_orientation = 90


## CURSROR

# Initialise Cursor
cursor_size = 4
cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")
# canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 5, fill=current_line_color, width=1)

# Move Cursor
def update_cursor():
    canvas.coords(cursor, coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size)


## STORING COMMANDS

def store_command(command, *args):
    list_of_commands.append((command, *args))
    print('Storing command:', command)

# Store Change Color Command
def store_color_command():
    new_color = colorchooser.askcolor(title="Choose color")
    # print("New Color:", new_color)

    if new_color[1]:
        # print("storing colour")
        store_command(change_line_color, new_color[1])


## GO 

def go():
    global go_flag
    go_flag = True

    print('now in go function')

    for command, *args in list_of_commands:
        command(*args)
        update_cursor()  
        window.update_idletasks()
        window.after(250)

    print(list_of_commands)
    go_flag = False
    # list_of_commands.clear()


## RESET VARIABLES

def reset_vars():
    global coords, cursor, current_line_color, current_line_width

    coords = [150, 150]
    current_line_color = "black"
    current_line_width = 1
    canvas.delete("all") 
    cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")


## PEN UP/DOWN

# Toggle Pen
def toggle_pen_state():
    global pen_state
    
    # store_command(toggle_pen_state)
    if go_flag:
        pen_state.set(1 - pen_state.get())




## LINE COLOR & THICKNESS

# Change Line Color
def change_line_color(new_color):
    global current_line_color

    if go_flag:
        # print(new_color)
        current_line_color = new_color


def change_line_width(new_width):
    global current_line_width

    if go_flag:
        current_line_width = int(new_width)
        print(current_line_width)



## MOVEMENT CONTROLS

# Move Up
def move_up():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 10, fill=current_line_color, width=current_line_width)
        # coords[1] += 10
        coords[1] -= 10
        # update_cursor()
        

# Move Down
def move_down():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0], coords[1] + 10, fill=current_line_color, width=current_line_width)
        # coords[1] -= 10
        coords[1] += 10
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


# Reset Orientation 
def reset_orientation():
    global current_orientation
    current_orientation = 90


# Set Angle for Rotation
def set_angle():
    rotation_angle = angle_entry.get()
    # print(rotation_angle)
    return int(rotation_angle)


# Set Orientation using Angle
def set_orientation(trig_angle, coords):
    if trig_angle < 0:
        print("trig value is too small", trig_angle)
        set_orientation(trig_angle + 360, coords)

    elif trig_angle == 90:
        # move up
        move_up()
        print("move up")

    elif trig_angle == 180:
        # move left
        move_left()
        print("move left")

    elif trig_angle == 270:
        # move down
        move_down()
        print("move down")

    elif trig_angle == 360:
        # move right
        move_right()
        print("move right")

    elif trig_angle > 360:
        print("trig value is larger than a full circle")
        set_orientation(trig_angle - 360, coords) 
    

    elif trig_angle > 0 and trig_angle < 90:
        # first quadrant
        print("first quadrant")
        a = trig_angle
        # - in y
        y_end = coords[1] - (10 * math.cos(math.radians(a)))
        # + in x
        x_end = coords[0] + (10 * math.sin(math.radians(a)))
    
    elif trig_angle > 90 and trig_angle < 180:
        # second quadrant
        print("second quadrant")
        a = trig_angle - 90
        # - in y
        y_end = coords[1] - (10 * math.cos(math.radians(a)))
        # - in x
        x_end = coords[0] - (10 * math.sin(math.radians(a)))
        
    elif trig_angle > 180 and trig_angle < 270:
        # third quadrant
        print("third quadrant")
        a = trig_angle - 180
        # + in y
        y_end = coords[1] + (10 * math.cos(math.radians(a)))
        # - in x
        x_end = coords[0] - (10 * math.sin(math.radians(a)))

    elif trig_angle > 270 and trig_angle < 360:
        # fourth quadrant
        print("fourth quadrant")
        a = trig_angle - 270
        # + in y
        y_end = coords[1] + (10 * math.cos(math.radians(a)))
        # + in x
        x_end = coords[0] + (10 * math.sin(math.radians(a)))

    return x_end, y_end



# Turn Left
def turn_left():
    # choose the angle then click turn left
    angle = set_angle()

    if go_flag:
        x, y = set_orientation(current_orientation + angle, coords)

        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], x, y, fill=current_line_color, width=current_line_width)
        coords[0] = x
        coords[1] = y


    

# Turn Right
def turn_right():
    # choose the angle then click turn right
    angle = set_angle()

    if go_flag:
        x, y = set_orientation(current_orientation - angle, coords)

        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], x, y, fill=current_line_color, width=current_line_width)
        coords[0] = x
        coords[1] = y



## SEQUENCING AND LOOPS

# Sequences
def set_sequence():
    global sequence_list
    
    # append every button pressed into list

    pass

# Loops
def replay():
    reset_vars()
    go()


def set_iterations():
    num = int(iterations.get())
    print(num)
    store_command(iterate, num)
    print("storing iteration number")
    return num


def iterate(num_of_iterations):
    reset_vars()
    print("iterating")
    if go_flag:
        for i in range(num_of_iterations):
            go()



## CLEAR MEMORY

def clear_memory():
    reset_vars()
    list_of_commands.clear()
    print('clear memory')

    
## BUTTONS

# Movement Controls
tk.Button(window, text="↑", command=lambda: store_command(move_up)).grid(column=0, row=1)
tk.Button(window, text="↓", command=lambda: store_command(move_down)).grid(column=1, row=1)
tk.Button(window, text="←", command=lambda: store_command(move_left)).grid(column=2, row=1)
tk.Button(window, text="→", command=lambda: store_command(move_right)).grid(column=3, row=1)
tk.Button(window, text="↰", command=lambda: store_command(turn_left)).grid(column=1, row=2)
tk.Button(window, text="↱", command=lambda: store_command(turn_right)).grid(column=2, row=2)

# Change Color
tk.Button(window, text="Change Color", command=store_color_command).grid(column=0, row=3)

# Pen Up/Down
# tk.Button(window, text="Pen Up/Down", command=toggle_pen).grid(column=1, row=3)
tk.Checkbutton(window, onvalue=1, offvalue=0, height=2, width=10, text="Pen Up", command=lambda: store_command(toggle_pen_state)).grid(column=1, row=3)

# Choose Angle Input
tk.Button(window, text="Choose Angle:", command=set_angle).grid(column=2, row=3)
angle_entry = tk.Entry(window)
angle_entry.grid(column=3, row=3)

tk.Button(window, text="Reset Orientation", command=reset_orientation).grid(column=3, row=2)

# Line Thickness Slider
line_width = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Width", command=lambda slider_val: store_command(change_line_width, slider_val))
line_width.grid(column=0, row=4, columnspan=2)

# Sequences & Loops
tk.Button(window, text="[ Sequence ]", command=set_sequence).grid(column=0, row=5)
tk.Button(window, text="Replay", command=replay).grid(column=1, row=5)

tk.Label(window, text="Iterations:").grid(column=2, row=4)
iterations = tk.Spinbox(window, from_=1, to=10)
iterations.grid(column=3, row=4)
tk.Button(window, text="Set Iteration", command=set_iterations, bg="grey").grid(column=3, row=5)

# Go & clear_memory
tk.Button(window, text="GO", command=go, bg="green").grid(column=2, row=6)
tk.Button(window, text="CM", command=clear_memory, bg="red").grid(column=0, row=6)

window.mainloop()