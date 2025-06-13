import cv2
import tkinter as tk
import time
from manual_mode_actions.keyboard_interface import keyboard_interface
from grid_gen_and_utils.red_mouse import red_mouse
from parameters import row, col, box_size, margine
from grid_gen_and_utils.Initialize import maze_board

def manual_mode(event):
    # Get current state from maze_board
    board = maze_board.get_board()
    current_row, current_col = maze_board.get_position()
    
    # Clear old position using the new method
    maze_board.clear_board()
    
    # Get move direction from keyboard
    row_change, col_change = keyboard_interface(event)
    
    # Update position
    current_row += row_change
    current_col += col_change
    # Keep within bounds
    current_row = max(0, min(current_row, row - 1))
    current_col = max(0, min(current_col, col - 1))
    
    # Update position in shared board

    
    # Update display
    print(f"Current Position: ({current_row}, {current_col})")
    maze_board.update_position(current_row, current_col)
    
    # Check for completion
    if current_row == row - 1 and current_col == col - 1:
        print("Reached the end of the maze!")
        maze_board.get_window().quit()
