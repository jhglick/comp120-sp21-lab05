"""
Module: draw.py 

Author:
COMP 120 class
Department of Computer Science
University of San Diego

Description:
A simple drawing program using Tkinter
"""

# Imports
import tkinter as tk
    
class Draw:
    def __init__(self):
        # Set up window
        self.window = tk.Tk() 
        self.window.title("Drawing Program") 

        # Set default line color and thickness
        self.color = "black"
        self.line_width = 1
        
        # Place canvas in window
        self.canvas = tk.Canvas(self.window, width = 400, 
            height = 400, bg = "white")
        self.canvas.grid(row = 1, column = 1)
        
        # Bind canvas mouse events to handler.
        self.canvas.bind("<ButtonPress-1>", 
                self.mouse_press_handler)
        self.canvas.bind("<B1-Motion>", 
                self.mouse_motion_handler)

        # Create frame for color buttons
        color_frame = tk.Frame(self.window)
        color_frame.grid(row = 2, column = 1)

        # Put color buttons in color frame.
        red_button = tk.Button(color_frame, text = 'red',
                    command = self.red, 
                    highlightbackground = 'red')
        red_button.grid(row = 1, column = 1)

        blue_button = tk.Button(color_frame, text = 'blue',
                    command = self.blue, 
                    highlightbackground = 'blue')
        blue_button.grid(row = 1, column = 2)

        green_button = tk.Button(color_frame, text = 'green',
                    command = self.green, 
                    highlightbackground = 'green')
        green_button.grid(row = 1, column = 3)

        yellow_button = tk.Button(color_frame, text = 'yellow',
                    command = self.yellow, 
                    highlightbackground = 'yellow')
        yellow_button.grid(row = 1, column = 4)

        black_button = tk.Button(color_frame, text = 'black',
                    command = self.black, 
                    highlightbackground = 'black')
        black_button.grid(row = 1, column = 5)

        # Create frame for line width slider
        line_width_slider_frame = tk.Frame(self.window)
        line_width_slider_frame.grid(row = 3, column = 1)

        line_width_slider = tk.Scale(line_width_slider_frame,
                    from_ = 1, to = 10, 
                    label = 'line width',
                    showvalue = 0,
                    orient = tk.HORIZONTAL)
        line_width_slider.grid(row = 1, column = 1)
        line_width_slider.configure(
                command = self.line_width_handler)

        # Create frame for clear and quit buttons
        button_frame = tk.Frame(self.window)
        button_frame.grid(row = 4, column = 1)

        clear_button = tk.Button(button_frame, 
                    text = "Clear",
                    command = self.clear_canvas)
        clear_button.grid(row = 1, column = 1)

        quit_button = tk.Button(button_frame, 
                text = "Quit",
                command = self.quit)
        quit_button.grid(row = 1, column = 2)

        # Start event loop
        self.window.mainloop() 
    
    def clear_canvas(self):
        # Clear the drawings in the canvas
        self.canvas.delete("line")

    def red(self):
        # Make line color red
        self.color = 'red'
    
    def blue(self):
        # Make line color blue
        self.color = 'blue'

    def green(self):
        # Make line color green
        self.color = 'green'

    def yellow(self):
        # Make line color yellow
        self.color = 'yellow'

    def black(self):
        # Make line color black
        self.color = 'black'

    def mouse_press_handler(self, event):
        # Handle mouse press in canvas
        self.prev_x = event.x
        self.prev_y = event.y

    def mouse_motion_handler(self, event):
        # Handle mouse movement in canvas
        cur_x = event.x
        cur_y = event.y
        self.canvas.create_line(self.prev_x, self.prev_y, 
                cur_x, cur_y, fill = self.color, 
                width = self.line_width, tags = "line")
        self.prev_x = cur_x
        self.prev_y = cur_y

    def quit(self):
        # Quit program
        self.window.destroy()

    def line_width_handler(self, value):
        # Handle change in line width
        self.line_width = int(value)
        print(type(self.line_width))

if __name__ == "__main__":
    # Create GUI
    Draw() 