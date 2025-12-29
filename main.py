import parameters
from utils.setup_dialog import get_settings

def main():
    grid_size, selected_solver = get_settings()
    if grid_size is None or selected_solver is None:
        return

    parameters.row = grid_size
    parameters.col = grid_size

    # Delay imports so parameters are set before MazeBoard initializes.
    from grid_gen_and_utils.Initialize import maze_board
    from manual_mode_actions.manual_mode import manual_mode
    from random_mode_actions.random_mode import random_mode
    from smarter_random_mode_actions.smarter_random_mode import smarter_random_mode
    from dijkstra_algorithm_mode_actions.dijkstra_mode import dijkstra_mode

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

if __name__ == "__main__":
    main()
