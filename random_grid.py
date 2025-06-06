import random

def random_grid_genrator(rows, cols):
    """
    Generates a random maze with a guaranteed path from top-left to bottom-right,
    moving only right or down.
    0 = path
    1 = wall
    """
    # Start with all walls
    maze = [[1 for _ in range(cols)] for _ in range(rows)]

    # Generate the path that goes only right or down
    r, c = 0, 0
    maze[r][c] = 0
    while r < rows - 1 or c < cols - 1:
        if r == rows - 1:
            c += 1
        elif c == cols - 1:
            r += 1
        else:
            if random.choice([True, False]):
                c += 1
            else:
                r += 1
        maze[r][c] = 0

    # Fill in other spaces randomly (excluding the path)
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] != 0:
                maze[i][j] = random.choice([0, 1])

    return maze

    #return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

#maze format:
# maze = [
#     [1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,1],
#     [1,0,1,1,1,1,0,1],
#     [1,0,1,0,0,1,0,1],
#     [1,0,1,0,1,1,0,1],
#     [1,0,1,0,0,0,0,1],
#     [1,0,0,0,1,1,0,1],
#     [1,1,1,1,1,1,1,1]
# ]
