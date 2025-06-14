from parameters import next_random_move, row, col, box_size, margine
from grid_gen_and_utils.Initialize import maze_board
from manual_mode_actions.manual_mode import manual_mode
from random_mode_actions.random_mode import random_mode
from smarter_random_mode_actions.smarter_random_mode import smarter_random_mode

def select_mode():
    print("\n=== Maze Solver Mode Selection ===")
    print("1. Manual Mode (Control with keyboard)")
    print("2. Random Mode (Basic random movement)")
    print("3. Smarter Random Mode (Enhanced random movement)")
    
    while True:
        try:
            choice = int(input("\nSelect a mode (1-3): "))
            if choice == 1:
                return "manual_mode"
            elif choice == 2:
                return "random_mode"
            elif choice == 3:
                return "smarter_random_mode"
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("Please enter a valid number")

# Get user's mode selection
selected_solver = select_mode()

if selected_solver == "manual_mode":
    # Manual key binds to manual_mode
    maze_board.get_window().bind('<Key>', manual_mode)

if selected_solver == "random_mode":
    # Start automatic simulation
    maze_board.get_window().after(100, lambda: random_mode())

if selected_solver == "smarter_random_mode":
    # Start automatic simulation with smarter approach
    maze_board.get_window().after(100, lambda: smarter_random_mode())

# Start the main event loop
maze_board.get_window().mainloop() 


