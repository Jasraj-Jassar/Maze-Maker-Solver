from types import SimpleNamespace
from dijkstra_algorithm_mode_actions.dijkstra_solver import dijkstra_solver
from grid_gen_and_utils.Initialize import maze_board
from grid_gen_and_utils.updatePos import update_position

dijkstra_path = None
dijkstra_index = 0


def dijkstra_mode(event=None):
    global dijkstra_path, dijkstra_index

    if dijkstra_path is None:
        maze = maze_board.get_maze()
        if not maze or not maze[0]:
            print("No maze data found for Dijkstra's algorithm")
            return

        start_x, start_y = maze_board.get_position()
        rows = len(maze)
        cols = len(maze[0])
        goal = (cols - 1, rows - 1)

        if (start_x, start_y) == goal:
            print("Already at the goal")
            return

        dijkstra_path = dijkstra_solver(maze, (start_x, start_y), goal)
        dijkstra_index = 0

        if not dijkstra_path:
            print("No path found by Dijkstra's algorithm")
            return

    if dijkstra_index >= len(dijkstra_path):
        print("Dijkstra's algorithm finished")
        return

    next_move = dijkstra_path[dijkstra_index]
    dijkstra_index += 1
    print(f"Simulating keypress: {next_move}")
    update_position(SimpleNamespace(keysym=next_move))

    maze_board.get_window().after(100, lambda: dijkstra_mode())
