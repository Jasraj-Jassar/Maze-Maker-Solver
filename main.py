import cv2
import tkinter as tk
from types import SimpleNamespace

from grid import make_grid
from remove_line import clear_grid_line
from standardize import standardize_start_end
from random_grid import random_grid_genrator
from keyboard_interface import keyboard_interface
from moveit_mouse import red_mouse

from cv_operations.capture_canvas import capture_canvas
from cv_operations.img_processing import img_processing


# Initialize main window
intialize = True
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


#initialize openvcv window  
canvas_img = capture_canvas(board)
cv2.imshow("Maze Capture", canvas_img)
cv2.waitKey(1)

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
    print(f"Current Position: ({current_row}, {current_col})")
    red_mouse(current_row, current_col, margine, box_size, board, color = 'red',)
    #capture the canvas and display it using OpenCV
    canvas_img = capture_canvas(board)
    img_processing(canvas_img)
    
    if current_row == row - 1 and current_col == col - 1: # when the mouse reaches the end of the maze it quits the program
        print("Reached the end of the maze!")
        window.quit()


def simulate_keypress_after_render():
    window.update()
    window.update_idletasks()
    fake_event = SimpleNamespace(keysym='enter')
    on_key(fake_event)


# Always bind key events
window.bind('<Key>', on_key)

# Conditionally simulate keypress after GUI has rendered
if intialize:
    intialize = False
    window.after(100, simulate_keypress_after_render)


# Start the main event loop
window.mainloop() 