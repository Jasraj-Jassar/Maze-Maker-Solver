from types import SimpleNamespace
from smarter_random_mode_actions.smarter_random_solver import smarter_random_solver
from parameters import next_random_move
from grid_gen_and_utils.Initialize import maze_board
from utils.updatePos import update_position

def smarter_random_mode(event=None):
    global next_random_move  # Add this to access the global variable
    
    # Get move direction
    print(f"Simulating keypress: {next_random_move}")

    if next_random_move is None:
        # If no valid move was found, try again after a short delay
        maze_board.get_window().after(100, lambda:smarter_random_mode())
        return
    
    # moves to the next position based on next_random_move using update_position
    update_position(SimpleNamespace(keysym=next_random_move))
    
    # Get next move from the maze grid
    maze = maze_board.get_maze()
    current_pos = maze_board.get_position()
    next_random_move = smarter_random_solver(maze, current_pos)
    
    # Schedule next move if this was a simulated move
    maze_board.get_window().after(100, lambda:smarter_random_mode()) 
