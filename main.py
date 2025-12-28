from grid_gen_and_utils.Initialize import maze_board
from manual_mode_actions.manual_mode import manual_mode
from random_mode_actions.random_mode import random_mode
from smarter_random_mode_actions.smarter_random_mode import smarter_random_mode
from dijkstra_algorithm_mode_actions.dijkstra_mode import dijkstra_mode

def select_mode():
    print("\n=== Maze Solver Mode Selection ===")
    print("1. Manual Mode (Control with keyboard)")
    print("2. Random Mode (Basic random movement)")
    print("3. Smarter Random Mode (Enhanced random movement)")
    print("4. Dijkstra Mode (Shortest path)")
    
    while True:
        try:
            choice = int(input("\nSelect a mode (1-4): "))
            if choice > 0 and choice < 5:
                return choice
        except ValueError:
            print("Please enter a valid number")

# Get user's mode selection
selected_solver = select_mode()


window = maze_board.get_window()
SOLVERS = {
    1: lambda: window.bind("<Key>", manual_mode),
    2: lambda: window.after(100, random_mode),
    3: lambda: window.after(100, smarter_random_mode),
    4: lambda: window.after(100, dijkstra_mode),
}

SOLVERS[selected_solver]()


# Start the main event loop
window.mainloop() 

