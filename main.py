from parameters import selected_solver, next_random_move, row, col, box_size, margine
from grid_gen_and_utils.Initialize import maze_board
from manual_mode_actions.manual_mode import manual_mode
from random_mode_actions.random_mode import random_mode


if selected_solver == "manual_mode":
    # Manual key binds to manual_mode
    maze_board.get_window().bind('<Key>', manual_mode)

if selected_solver == "smatter_approach":
    # Start automatic simulation
    maze_board.get_window().after(100, lambda: random_mode(is_simulated=True))

# Start the main event loop
maze_board.get_window().mainloop() 


