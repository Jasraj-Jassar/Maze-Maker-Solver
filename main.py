import tkinter as tk
import cv2
from grid import make_grid
from remove_line import clear_grid_line
from standardize import standardize_start_end
from random_grid import random_grid_genrator
from keyboard_interface import keyboard_interface
from moveit_mouse import red_mouse
from capture_canvas import capture_canvas


# Initialize main window
window = tk.Tk()

# Define grid dimensions
row = 8  # Number of rows
col = row  # Number of columns, assuming a square grid
box_size = row * 10 # Size of each grid cell
margine = box_size

maze = random_grid_genrator(row, col)
# Create the grid and standardize start/end positions
board = make_grid(maze, margine, box_size, window)
standard_start_end = standardize_start_end(row, col, margine, box_size, board)

# Initialize position
current_row = 0
current_col = 0
red_mouse(current_row, current_col, margine, box_size, board, color='red')


def on_key(event):
    global current_row, current_col
    red_mouse(current_row, current_col, margine, box_size, board, color = 'black')
    row_change, col_change = keyboard_interface(event)
    current_row += row_change
    current_col += col_change
    # Keep within bounds
    current_row = max(0, min(current_row, row - 1))
    current_col = max(0, min(current_col, col - 1))
    # Update mouse position
    red_mouse(current_row, current_col, margine, box_size, board, color = 'red',)

    #capture the canvas and display it using OpenCV
    canvas_img = capture_canvas(board)
    cv2.imshow("Maze Capture", canvas_img)
    cv2.waitKey(1)


# Bind keyboard events
window.bind('<Key>', on_key)

# Start the main event loop
window.mainloop() 