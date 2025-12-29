import random


#Random maze solver it will use random moves to find a path from the start till the end of the maze.
#Parent - random_maze_solver 
#Child - smarter_random_solver - biases moves toward the goal.

def smarter_random_solver(maze, position):
    if not maze or not maze[0]:
        return None

    x, y = position
    rows = len(maze)
    cols = len(maze[0])
    goal_x, goal_y = cols - 1, rows - 1

    directions = {
        "Up": (x, y - 1),
        "Down": (x, y + 1),
        "Left": (x - 1, y),
        "Right": (x + 1, y),
    }

    best_moves = []
    best_dist = None
    valid_moves = []

    for direction, (nx, ny) in directions.items():
        if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == 0:
            valid_moves.append(direction)
            dist = abs(goal_x - nx) + abs(goal_y - ny)
            if best_dist is None or dist < best_dist:
                best_dist = dist
                best_moves = [direction]
            elif dist == best_dist:
                best_moves.append(direction)

    if best_moves:
        return random.choice(best_moves)
    return random.choice(valid_moves) if valid_moves else None
