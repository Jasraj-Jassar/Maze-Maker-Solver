
def clear_grid_line(x, y, box_size, board):
    # Draw left border of square (2,2) in red
    x = x * box_size
    y = y * box_size
    board.create_line(x, y, x, y + box_size, fill='black', width=4)
    return board