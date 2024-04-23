import tkinter as tk
from tkinter import colorchooser
from tkinter import *
import math

window = tk.Tk()

coords = [150, 150]

canvas = tk.Canvas(window, bg="white", height=300, width=300)
canvas.grid(column=0, row=0, columnspan=4)

# Initialise Cursor
cursor_size = 4
cursor = canvas.create_oval(coords[0] - cursor_size, coords[1] - cursor_size, coords[0] + cursor_size, coords[1] + cursor_size, fill="red", outline="red")

canvas.create_line(coords[0], coords[1], coords[0], coords[1] - 10, fill="blue")

# SPEC: Turtle should be able to change line colour
current_line_color = "black"

# Change Line Width
current_line_width = 1

current_orientation = 90

angle = 135

if angle < 90:
    diff = current_orientation - angle
    trig_angle = current_orientation - diff
elif angle > 90:
    trig_angle = current_orientation - angle

print(trig_angle)


def set_orientation(trig_angle):
    if trig_angle < 0:
        print("trig value is negative")
        set_orientation(trig_angle + 360)
    
    elif trig_angle == 90:
        # move up
        x_end = coords[0]
        y_end = coords[1]-100
        print("move up")

    elif trig_angle == 180:
        # move left
        x_end = coords[0]-100
        y_end = coords[1]
        print("move left")

    elif trig_angle == 270:
        # move down
        x_end = coords[0]
        y_end = coords[1]+100
        print("move down")

    elif trig_angle == 360 or trig_angle == 0:
        # move right
        x_end = coords[0]+100
        y_end = coords[1]
        print("move right")

    elif trig_angle > 360:
        print("trig value is more than a full circle")
        set_orientation(trig_angle - 360) 


    elif trig_angle > 0 and trig_angle < 90:
        # first quadrant
        print("first quadrant")
        a = trig_angle
        # - in y
        y_end = coords[1] - (100 * math.cos(math.radians(a)))
        # + in x
        x_end = coords[0] + (100 * math.sin(math.radians(a)))
    
    elif trig_angle > 90 and trig_angle < 180:
        # second quadrant
        print("second quadrant")
        a = trig_angle - 90
        # - in y
        y_end = coords[1] - (100 * math.cos(math.radians(a)))
        # - in x
        x_end = coords[0] - (100 * math.sin(math.radians(a)))
        
    elif trig_angle > 180 and trig_angle < 270:
        # third quadrant
        print("third quadrant")
        a = trig_angle - 180
        # + in y
        y_end = coords[1] + (100 * math.cos(math.radians(a)))
        # - in x
        x_end = coords[0] - (100 * math.sin(math.radians(a)))

    elif trig_angle > 270 and trig_angle < 360:
        # fourth quadrant
        print("fourth quadrant")
        a = trig_angle - 270
        # + in y
        y_end = coords[1] + (100 * math.cos(math.radians(a)))
        # + in x
        x_end = coords[0] + (100 * math.sin(math.radians(a)))

    return x_end, y_end



# Adjusting for tkinter coordinate system (positive y-axis downwards)
x_end = set_orientation(trig_angle)[0]
y_end = set_orientation(trig_angle)[1]

print(x_end)
print(y_end)

canvas.create_line(coords[0], coords[1], x_end, y_end, fill=current_line_color, width=current_line_width)
coords[0] = x_end
coords[1] = y_end




window.mainloop()
