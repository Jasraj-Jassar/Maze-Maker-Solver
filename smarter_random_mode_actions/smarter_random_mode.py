import cv2
from types import SimpleNamespace
from cv_operations.capture_canvas import capture_canvas
from cv_operations.mouse_pos_opencv import mouse_pos_opencv
from smarter_random_mode_actions.smarter_random_solver import smarter_random_solver
from parameters import next_random_move
from grid_gen_and_utils.Initialize import maze_board
from grid_gen_and_utils.updatePos import update_position

def smarter_random_mode(event=None):
    global next_random_move  # Add this to access the global variable
    
    # Get current state
    board = maze_board.get_board()
    
    # Get move direction
    print(f"Simulating keypress: {next_random_move}")

    if next_random_move is None:
        # If no valid move was found, try again after a short delay
        maze_board.get_window().after(100, lambda:smarter_random_mode())
        return
    
    # moves to the next position based on next_random_move using update_position
    update_position(SimpleNamespace(keysym=next_random_move))
    
    # Process image and get next move
    canvas_img = capture_canvas(board)
    canvas_mouse_pos, circles_pos = mouse_pos_opencv(canvas_img)
    next_random_move = smarter_random_solver(canvas_mouse_pos, circles_pos)
    # Update OpenCV window
    cv2.imshow("Maze smarter_random_mode", canvas_mouse_pos)
    cv2.waitKey(1)
    
    # Schedule next move if this was a simulated move
    maze_board.get_window().after(100, lambda:smarter_random_mode()) 