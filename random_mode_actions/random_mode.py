import cv2
from types import SimpleNamespace
from manual_mode_actions.keyboard_interface import keyboard_interface
from cv_operations.capture_canvas import capture_canvas
from cv_operations.mouse_pos_opencv import mouse_pos_opencv
from random_mode_actions.random_solver import random_solver
from parameters import row, col, next_random_move
from grid_gen_and_utils.Initialize import maze_board

def random_mode(event=None):
    global next_random_move  # Add this to access the global variable
    
    # Get current state
    board = maze_board.get_board()
    current_row, current_col = maze_board.get_position()
    
    # Get move direction

    print(f"Simulating keypress: {next_random_move}")
    row_change, col_change = keyboard_interface(SimpleNamespace(keysym=next_random_move))

    # Update position
    current_row += row_change
    current_col += col_change
    # Keep within bounds
    current_row = max(0, min(current_row, row - 1))
    current_col = max(0, min(current_col, col - 1))
    # Update display
    print(f"Current Position: ({current_row}, {current_col})")
    maze_board.clear_board()
    maze_board.update_position(current_row, current_col)
    
    # Check for completion
    if current_row == row - 1 and current_col == col - 1:
        print("Reached the end of the maze!")
        maze_board.get_window().quit()
        return
    
    # Process image and get next move
    canvas_img = capture_canvas(board)
    canvas_mouse_pos, circles_pos = mouse_pos_opencv(canvas_img)
    next_random_move = random_solver(canvas_mouse_pos, circles_pos)
    

    # Update OpenCV window
    cv2.imshow("Maze Capture", canvas_mouse_pos)
    cv2.waitKey(1)
    
    # Schedule next move
    maze_board.get_window().after(100, lambda: random_mode()) 