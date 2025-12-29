import random


#Random maze solver it will use random moves to find a path from the start till the end of the maze.
def random_solver(maze, position):
    if not maze or not maze[0]:
        return None

    x, y = position
    rows = len(maze)
    cols = len(maze[0])

    directions = {
        "Up": (x, y - 1),
        "Down": (x, y + 1),
        "Left": (x - 1, y),
        "Right": (x + 1, y),
    }

    valid_moves = [
        direction
        for direction, (nx, ny) in directions.items()
        if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == 0
    ]

    return random.choice(valid_moves) if valid_moves else None
