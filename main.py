import cv2
import time
from types import SimpleNamespace

from keyboard_interface import keyboard_interface
from moveit_mouse import red_mouse
from cv_operations.capture_canvas import capture_canvas
from cv_operations.img_processing import img_processing
from cv_operations.random_solver import random_solver
from parameters import selected_solver, next_random_move, row, col, box_size, margine
from Initialize import maze_board
from manual_mode import manual_mode

def handle_move(event=None, is_simulated=False):
    global next_random_move  # Add this to access the global variable
    
    # Get current state
    board = maze_board.get_board()
    current_row, current_col = maze_board.get_position()
    
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
    
    # Update position in shared board
    maze_board.update_position(current_row, current_col)
    
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
        maze_board.get_window().quit()
        return
    
    # Update OpenCV window
    cv2.imshow("Maze Capture", canvas_mouse_pos)
    cv2.waitKey(1)
    
    # Schedule next move if this was a simulated move
    if is_simulated:
        maze_board.get_window().after(100, lambda: handle_move(is_simulated=True))

if selected_solver == "manual_mode":
    # Manual key binds to handle_move
    maze_board.get_window().bind('<Key>', manual_mode)

if selected_solver == "smatter_approach":
    # Start automatic simulation
    maze_board.get_window().after(100, lambda: handle_move(is_simulated=True))

# Start the main event loop
maze_board.get_window().mainloop() 


