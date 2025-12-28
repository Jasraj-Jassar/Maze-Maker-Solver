import heapq


def dijkstra_solver(maze, start, goal):
    """
    Returns a list of moves ("Up", "Down", "Left", "Right") for the shortest path.
    Coordinates are (x, y) where maze[y][x] is the cell.
    """
    if not maze or not maze[0]:
        return []

    rows = len(maze)
    cols = len(maze[0])

    def is_open(x, y):
        return 0 <= x < cols and 0 <= y < rows and maze[y][x] == 0

    if not is_open(*start) or not is_open(*goal):
        return []

    distances = {start: 0}
    previous = {}
    heap = [(0, start)]
    visited = set()

    while heap:
        current_dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        x, y = current
        neighbors = [
            (x, y - 1),
            (x, y + 1),
            (x - 1, y),
            (x + 1, y),
        ]

        for neighbor in neighbors:
            nx, ny = neighbor
            if not is_open(nx, ny) or neighbor in visited:
                continue
            new_dist = current_dist + 1
            if new_dist < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(heap, (new_dist, neighbor))

    if goal not in distances:
        return []

    path = []
    node = goal
    while node != start:
        path.append(node)
        node = previous.get(node)
        if node is None:
            return []
    path.append(start)
    path.reverse()

    moves = []
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        dx = x2 - x1
        dy = y2 - y1
        if dx == 1 and dy == 0:
            moves.append("Right")
        elif dx == -1 and dy == 0:
            moves.append("Left")
        elif dx == 0 and dy == 1:
            moves.append("Down")
        elif dx == 0 and dy == -1:
            moves.append("Up")

    return moves
