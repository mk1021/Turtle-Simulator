import tkinter as tk
from tkinter import colorchooser
from tkinter import *
import math
from tkinter import Menubutton, Menu
from tkinter import messagebox


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

# Current Orientation (0: right, 90: up, 180: left, 270: down)
current_orientation = 90


#####################################################################################
## CURSROR

# Initialise Cursor
cursor_size = 4
cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="dark green", outline="dark green")

# Move Cursor
def update_cursor():
    canvas.coords(cursor, coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size)



#####################################################################################
## STORING COMMANDS

# Store Command
def store_command(command, *args):
    list_of_commands.append((command, *args))

# Store Change Color Command
def store_color_command():
    new_color = colorchooser.askcolor(title="Choose color")

    if new_color[1]:
        store_command(change_line_color, new_color[1])



#####################################################################################
## GO 

def go():
    global go_flag
    go_flag = True
    
    for command, *args in list_of_commands:
        
        if command == iterate:
            index=list_of_commands.index((command, *args))
            iterate(*args, index)
        else:
            command(*args)
            update_cursor()  
            window.update_idletasks()
            window.after(250)

    go_flag = False



#####################################################################################
## RESET VARIABLES

def reset_vars():
    global coords, cursor, current_line_color, current_line_width

    coords = [150, 150]
    current_line_color = "black"
    current_line_width = 1
    line_width.set(1)
    angle_entry.delete(0, END)
    canvas.delete("all") 
    cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")



#####################################################################################
## LINE COLOR & THICKNESS

# Change Line Color
def change_line_color(new_color):
    global current_line_color

    if go_flag:
        current_line_color = new_color


def change_line_width(new_width):
    global current_line_width

    if go_flag:
        current_line_width = int(new_width)



#####################################################################################
## PEN UP/DOWN

# Toggle Pen
def toggle_pen_state():
    global pen_state
    
    if go_flag:
        pen_state.set(1 - pen_state.get())



#####################################################################################
## MOVEMENT CONTROLS

# Move Up
def move_up():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 10, fill=current_line_color, width=current_line_width)
        # coords[1] += 10
        coords[1] -= 10
        

# Move Down
def move_down():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0], coords[1] + 10, fill=current_line_color, width=current_line_width)
        # coords[1] -= 10
        coords[1] += 10
        

# Move Left
def move_left():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0] - 10, coords[1], fill=current_line_color, width=current_line_width)
        coords[0] -= 10
    

# Move Right
def move_right():
    if go_flag:
        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], coords[0] + 10, coords[1], fill=current_line_color, width=current_line_width)
        coords[0] += 10


# Reset Orientation 
def reset_orientation():
    global current_orientation
    current_orientation = 90


# Set Angle for Rotation
def set_angle():
    rotation_angle_str = angle_entry.get()
    rotation_angle = int(rotation_angle_str)
    angles.append(rotation_angle)
    angle_entry.delete(0, END)


# Set Orientation using Angle
def set_orientation(trig_angle, coords):
    trig_angle %= 360
    
    x_end, y_end = coords

    if trig_angle == 90:
        # move up
        move_up()

    elif trig_angle == 180:
        # move left
        move_left()

    elif trig_angle == 270:
        # move down
        move_down()

    elif trig_angle == 360 or trig_angle == 0:
        # move right
        move_right() 
    

    elif 0 < trig_angle < 90:
        # first quadrant
        a = trig_angle
        # - in y
        y_end = coords[1] - (10 * math.sin(math.radians(a)))
        # + in x
        x_end = coords[0] + (10 * math.cos(math.radians(a)))
    
    elif 90 < trig_angle < 180:
        # second quadrant
        a = trig_angle - 90
        # - in y
        y_end = coords[1] - (10 * math.cos(math.radians(a)))
        # - in x
        x_end = coords[0] - (10 * math.sin(math.radians(a)))
        
    elif 180 < trig_angle < 270:
        # third quadrant
        a = trig_angle - 180
        # + in y
        y_end = coords[1] + (10 * math.sin(math.radians(a)))
        # - in x
        x_end = coords[0] - (10 * math.cos(math.radians(a)))

    elif 270 < trig_angle < 360:
        # fourth quadrant
        a = trig_angle - 270
        # + in y
        y_end = coords[1] + (10 * math.cos(math.radians(a)))
        # + in x
        x_end = coords[0] + (10 * math.sin(math.radians(a)))


    return x_end, y_end


# Turn Left
def turn_left():
    global current_orientation

    if go_flag:
        x, y = set_orientation(current_orientation + angles[0], coords)

        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], x, y, fill=current_line_color, width=current_line_width)
        coords[0] = x
        coords[1] = y

        angles.append(angles.pop(0))


# Turn Right
def turn_right():
    global current_orientation

    if go_flag:
        x, y = set_orientation(current_orientation - angles[0], coords)

        if pen_state.get() == 1:
            canvas.create_line(coords[0], coords[1], x, y, fill=current_line_color, width=current_line_width)
        coords[0] = x
        coords[1] = y

        angles.append(angles.pop(0))



#####################################################################################
## ITERATIONS & LOOPS

# Loops
def replay():
    reset_vars()
    window.after(500)
    go()


# Iterations
def set_iterations():
    num = int(iterations.get())
    store_command(iterate, num)


def iterate(num_of_iterations, index):
    global current_line_color, current_line_width
    iterate_sequence = list_of_commands[:index]

    if go_flag:

        for i in range(num_of_iterations-1):

            current_line_color = "black"
            current_line_width = 1
            line_width.set(1)
            
            for command, *args in iterate_sequence:
                if command == iterate:
                    continue
                
                command(*args)
                update_cursor()  
                window.update_idletasks()
                window.after(250)



#####################################################################################
## PAUSE

def pause(seconds):
    into_ms = seconds * 1000
    window.after(into_ms)

# Select Pause Duration
def set_pause_duration(seconds):
    pause_menu.config(text=f"Pause Duration ({seconds} seconds)")
    store_command(pause, seconds)



#####################################################################################
## CLEAR MEMORY

def clear_memory():
    reset_vars()
    list_of_commands.clear()
    angles.clear()
    # print('clear memory')



#####################################################################################
## HELP MENUBAR

def welcome_page():
    welcome_page = tk.Toplevel(window)
    welcome_page.title("Welcome")

    welcome_message = "Welcome to the Turtle Graphics Application!\nPlease click the Instructions button to learn how to use this application."
    tk.Label(welcome_page, text=welcome_message, padx=20, pady=20).pack()

    tk.Button(welcome_page, text="Instructions", command=instructions).pack()
    tk.Button(welcome_page, text="Close", command=welcome_page.destroy).pack()



def instructions():
    instructions_page = tk.Toplevel(window)
    instructions_page.title("Instructions: How to use the application")

    instructions_text = """
    Welcome to the Turtle Graphics Application!

    Instructions:
    
    1. Movement Controls:
       - Use the arrow buttons (↑, ↓, ←, →) to move the turtle cursor in the respective direction.
    
    2. Rotation Control:
       - Enter an angle in degrees and click the 'Set Angle' button to specify the angle for turning left or right.
       - Then click the buttons (↰ and ↱) to turn left or right, respectively.
       - After clicking the button, the rotation angle is set back to 0, therefore please re-Enter the re-set the angle for each time the turn left or right buttons are used. 

    3. Change Line Color and Width:
       - The 'Change Color' button will let you choose a new line color.
       - Adjust the 'Line Width' slider to change the width of the lines.

    4. Pen Up/Down:
       - Use the 'Pen Up' checkbox to toggle and control whether the turtle draws lines as it moves.

    5. Iterations (Loops):
       - Enter the number of iterations in the 'Iterations' Spinbox and click 'Set Iteration' to repeat a sequence of commands.

    6. Replay:
       - Click the 'Replay' button to see the application draw your drawing again.

    7. Pause Duration:
       - By clicking the 'Pause Duration' button, there'll be a drop menu to select the duration for pausing the execution of commands.

    8. Go:
       - Once all commands have been added, click the green 'Go' button to see the application draw!
    
    9. Clear Memory:
       - Entered your commands in wrong? Just Click the red clear memory ('CM') button to clear the instructions and start again.
       - Be sure to click the 'CM' button before you start. 

    10. Using Menus:
       - Explore the 'File' menu for options like New, and Exit.
       - The 'Help' menu provides access to the Welcome message and these instructions.


    Enjoy creating your drawings!
    """

    tk.Label(instructions_page, text=instructions_text, padx=20, pady=20, justify="left").pack()

    tk.Button(instructions_page, text="I understand", command=instructions_page.destroy).pack()



#####################################################################################    
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
tk.Checkbutton(window, onvalue=1, offvalue=0, height=2, width=10, text="Pen Up", command=lambda: store_command(toggle_pen_state)).grid(column=3, row=6)

# Choose Angle Input
tk.Button(window, text="Set Angle:", command=set_angle).grid(column=0, row=3)
angle_entry = tk.Entry(window)
angle_entry.grid(column=1, row=3)

# Line Thickness Slider
line_width = tk.Scale(window, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Width", command=lambda slider_val: store_command(change_line_width, slider_val))
line_width.grid(column=0, row=4, columnspan=2)

# Replay
tk.Button(window, text="Replay", command=replay).grid(column=2, row=6)

# Iterations (Loops)
tk.Label(window, text="Iterations:").grid(column=2, row=4)
iterations = tk.Spinbox(window, from_=1, to=10)
iterations.grid(column=3, row=4)
tk.Button(window, text="Set Iteration", command=set_iterations, bg="grey").grid(column=3, row=5)

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
tk.Button(window, text="CM", command=clear_memory, bg="red").grid(column=3, row=3)



##########################################################################################
## MENUBAR
menubar = Menu(window)
window.config(menu=menubar)

# File Menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=reset_vars)
file_menu.add_command(label="Exit", command=window.quit)

# Help Menu 
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Welcome", command=welcome_page)
help_menu.add_command(label="Instructions", command=instructions)



##########################################################################
## MAIN

window.mainloop()