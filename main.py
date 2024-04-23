import tkinter as tk
from tkinter import colorchooser
from tkinter import *
import math
from tkinter import Menubutton, Menu

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

# Turning Left/Right
angles = []

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

    # print('now in go function')

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
    line_width.set(1)
    angle_entry.delete(0, END)
    pen_state.set(0)
    canvas.delete("all") 
    cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")



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
    rotation_angle_str = angle_entry.get()
    rotation_angle = int(rotation_angle_str)
    #print(rotation_angle)
    angles.append(rotation_angle)
    print(angles)
    angle_entry.delete(0, END)


# Set Orientation using Angle
def set_orientation(trig_angle, coords):
    trig_angle %= 360
    
    x_end, y_end = coords

    if trig_angle == 90:
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

    elif trig_angle == 360 or trig_angle == 0:
        # move right
        move_right()
        print("move right") 
    

    elif 0 < trig_angle < 90:
        # first quadrant
        print("first quadrant")
        a = trig_angle
        # - in y
        y_end = coords[1] - (10 * math.sin(math.radians(a)))
        # + in x
        x_end = coords[0] + (10 * math.cos(math.radians(a)))
    
    elif 90 < trig_angle < 180:
        # second quadrant
        print("second quadrant")
        a = trig_angle - 90
        # - in y
        y_end = coords[1] - (10 * math.cos(math.radians(a)))
        # - in x
        x_end = coords[0] - (10 * math.sin(math.radians(a)))
        
    elif 180 < trig_angle < 270:
        # third quadrant
        print("third quadrant")
        a = trig_angle - 180
        # + in y
        y_end = coords[1] + (10 * math.sin(math.radians(a)))
        # - in x
        x_end = coords[0] - (10 * math.cos(math.radians(a)))

    elif 270 < trig_angle < 360:
        # fourth quadrant
        print("fourth quadrant")
        a = trig_angle - 270
        print(a)
        # + in y
        y_end = coords[1] + (10 * math.cos(math.radians(a)))
        print(y_end)
        # + in x
        x_end = coords[0] + (10 * math.sin(math.radians(a)))
        print(10 * math.sin(math.radians(a)))
        print(x_end)

    return x_end, y_end

# Turn Left
def turn_left():
    global current_orientation
    # choose the angle then click turn left
    # angles = set_angle()
    # current_orientation += angle - this is right but have to implement more stuff before using it
    # print(current_orientation)
    print("turning left")

    if go_flag:
        x, y = set_orientation(current_orientation + angles[0], coords)

        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], x, y, fill=current_line_color, width=current_line_width)
        coords[0] = x
        coords[1] = y

        angles.append(angles.pop(0))
        print(angles)



# Turn Right
def turn_right():
    global current_orientation
    # choose the angle then click turn right
    # angles = set_angle()
    # current_orientation -= angle
    # print(current_orientation)
    print("turning right")

    if go_flag:
        x, y = set_orientation(current_orientation - angles[0], coords)

        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], x, y, fill=current_line_color, width=current_line_width)
        coords[0] = x
        coords[1] = y

        angles.append(angles.pop(0))
        print(angles)



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
    print("storing iteration number", num)
    return num


def iterate(num_of_iterations):
    reset_vars()
    print("iterating")
    if go_flag:
        for i in range(num_of_iterations):
            go()


## PAUSE

def pause(seconds):
    into_ms = seconds * 1000
    window.after(into_ms)


# Select Pause Duration
def set_pause_duration(seconds):
    pause_menu.config(text=f"Pause Duration ({seconds} seconds)")
    store_command(pause, seconds)



## CLEAR MEMORY

def clear_memory():
    reset_vars()
    list_of_commands.clear()
    angles.clear()
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
tk.Button(window, text="Change Color", command=store_color_command).grid(column=0, row=6)

# Pen Up/Down
# tk.Button(window, text="Pen Up/Down", command=toggle_pen).grid(column=1, row=3)
tk.Checkbutton(window, onvalue=1, offvalue=0, height=2, width=10, text="Pen Up", command=lambda: store_command(toggle_pen_state)).grid(column=3, row=6)

# Choose Angle Input
tk.Button(window, text="Angle:", command=set_angle).grid(column=2, row=3)
angle_entry = tk.Entry(window)
angle_entry.grid(column=3, row=3)

tk.Button(window, text="Reset Orientation", command=reset_orientation).grid(column=0, row=3)

# Line Thickness Slider
line_width = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Width", command=lambda slider_val: store_command(change_line_width, slider_val))
line_width.grid(column=0, row=4, columnspan=2)

# Sequences & Loops
# tk.Button(window, text="[ Sequence ]", command=set_sequence).grid(column=0, row=5)
tk.Button(window, text="Replay", command=replay).grid(column=2, row=6)


tk.Label(window, text="Iterations:").grid(column=2, row=4)
iterations = tk.Spinbox(window, from_=1, to=10)
iterations.grid(column=3, row=4)
tk.Button(window, text="Set Iteration", command=set_iterations, bg="grey").grid(column=3, row=5)

# tk.Button(window, text="Random button", command=set_iterations, bg="grey").grid(column=3, row=6)


# Pause Menubutton
pause_menu = Menubutton(window, text="Pause Duration (seconds)")
pause_menu.grid(column=1, row=6)

# create a menu 
pause_menu.menu = Menu(pause_menu, tearoff=0)
pause_menu["menu"] = pause_menu.menu

pause_menu.menu.add_command(label="1 second", command=lambda: set_pause_duration(1))
pause_menu.menu.add_command(label="2 seconds", command=lambda: set_pause_duration(2))
pause_menu.menu.add_command(label="3 seconds", command=lambda: set_pause_duration(3))
pause_menu.menu.add_command(label="5 seconds", command=lambda: set_pause_duration(5))
pause_menu.menu.add_command(label="10 seconds", command=lambda: set_pause_duration(10))
pause_menu.menu.add_command(label="100 seconds", command=lambda: set_pause_duration(100))


# Go & clear_memory
tk.Button(window, text="GO", command=go, bg="green").grid(column=3, row=2)
tk.Button(window, text="CM", command=clear_memory, bg="red").grid(column=0, row=2)

window.mainloop()