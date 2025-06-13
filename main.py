import cv2
import tkinter as tk
import time
from types import SimpleNamespace

from grid import make_grid
from remove_line import clear_grid_line
from standardize import standardize_start_end
from random_grid import random_grid_genrator
from keyboard_interface import keyboard_interface
from moveit_mouse import red_mouse

from cv_operations.capture_canvas import capture_canvas
from cv_operations.img_processing import img_processing
from cv_operations.random_solver import random_solver
from cv_operations.smatter_solver import smatter_solver
from cv_operations.goal_recognizer import goal_recognizer


# Paramenters
next_random_move = 'enter'
selected_solver = 'smatter_approach'  # Set the solver type
row = 8  # Number of rows - Defines grid dimensions
col = row  # Number of columns, assuming a square grid
box_size = row * 10 # Size of each grid cell
margine = box_size

# Initialize main window
window = tk.Tk()
maze = random_grid_genrator(row, col)
# Create the grid and standardize start/end positions
board = make_grid(maze, margine, box_size, window)
standard_start_end = standardize_start_end(margine, box_size, board, row, col)

# Initialize position
board, current_row, current_col = red_mouse(margine, box_size, board) # this will use default params in the moveit_mouse.py


#initialize openvcv window  
canvas_img = capture_canvas(board)
cv2.imshow("Maze Capture", canvas_img)
cv2.waitKey(1)

def handle_move(event=None, is_simulated=False):
    
    global current_row, current_col, next_random_move
    
    # Clear old position
    red_mouse(margine, box_size, board, "black", current_row, current_col)
    
    # Get move direction
    if is_simulated:
        print(f"Simulating keypress: {next_random_move}")
        row_change, col_change = keyboard_interface(SimpleNamespace(keysym=next_random_move))
    else:
        row_change, col_change = keyboard_interface(event)
    
    # Update position
    current_row += row_change
    current_col += col_change
    # Keep within bounds
    current_row = max(0, min(current_row, row - 1))
    current_col = max(0, min(current_col, col - 1))
    
    # Update display
    print(f"Current Position: ({current_row}, {current_col})")
    red_mouse(margine, box_size, board, "red", current_row, current_col)
    
    # Process image and get next move
    canvas_img = capture_canvas(board)
    canvas_mouse_pos, circles_pos = img_processing(canvas_img)
    next_random_move = random_solver(canvas_mouse_pos, circles_pos)
    
    # Check for completion
    if current_row == row - 1 and current_col == col - 1:
        print("Reached the end of the maze!")
        window.quit()
        return
    
    # Update OpenCV window
    cv2.imshow("Maze Capture", canvas_mouse_pos)
    cv2.waitKey(1)
    
    # Schedule next move if this was a simulated move
    if is_simulated:
        window.after(100, lambda: handle_move(is_simulated=True))

# Start automatic simulation
window.after(100, lambda: handle_move(is_simulated=True))

# Start the main event loop
window.mainloop() 


# # Always bind key events
# window.bind('<Key>', handle_move) - this is manual comtrol TODO Later 