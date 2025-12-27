import cv2
from types import SimpleNamespace
from cv_operations.capture_canvas import capture_canvas
from cv_operations.mouse_pos_opencv import mouse_pos_opencv
from random_mode_actions.random_solver import random_solver
from parameters import next_random_move
from grid_gen_and_utils.Initialize import maze_board
from grid_gen_and_utils.updatePos import update_position

def random_mode(event=None):
    global next_random_move  # Add this to access the global variable
    
    # Get current state
    board = maze_board.get_board()

    # moves to the next position based on next_random_move
    print(f"Simulating keypress: {next_random_move}")
    update_position(SimpleNamespace(keysym=next_random_move))

    # Process image and get next move
    canvas_img = capture_canvas(board)
    canvas_mouse_pos, circles_pos = mouse_pos_opencv(canvas_img)
    next_random_move = random_solver(canvas_mouse_pos, circles_pos)
    

    # Update OpenCV window
    cv2.imshow("Maze Capture", canvas_mouse_pos)
    cv2.waitKey(1)
    
    # Schedule next move
    maze_board.get_window().after(100, lambda: random_mode()) 