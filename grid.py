import tkinter as tk
def make_grid(grid, box_size, window):
    """
    Creates a grid of boxes on the given window with proper margins.
    """
    margin = box_size  # Define consistent margin
    rows, cols = len(grid), len(grid[0])

    canvas_width = cols * box_size + 2 * margin
    canvas_height = rows * box_size + 2 * margin

    window.configure(bg='black')
    board = tk.Canvas(window, width=canvas_width, height=canvas_height,
                      bg='black', highlightthickness=0)
    board.pack()

    for y in range(rows):
        for x in range(cols):
            color = 'white' if grid[y][x] == 1 else 'black'
            x1 = x * box_size + margin
            y1 = y * box_size + margin
            x2 = x1 + box_size
            y2 = y1 + box_size
            board.create_rectangle(x1, y1, x2, y2, fill=color, outline='gray')

    return board