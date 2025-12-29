from types import SimpleNamespace
from random_mode_actions.random_solver import random_solver
from parameters import next_random_move
from grid_gen_and_utils.Initialize import maze_board
from utils.updatePos import update_position

def random_mode(event=None):
    global next_random_move  # Add this to access the global variable
    
    # moves to the next position based on next_random_move
    print(f"Simulating keypress: {next_random_move}")
    update_position(SimpleNamespace(keysym=next_random_move))

    # Get next move from the maze grid
    maze = maze_board.get_maze()
    current_pos = maze_board.get_position()
    next_random_move = random_solver(maze, current_pos)
    
    # Schedule next move
    maze_board.get_window().after(100, lambda: random_mode()) 
