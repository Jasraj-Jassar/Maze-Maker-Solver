def clear_grid_line(x, y, box_size, margin, board):
    """
    Removes a vertical line from the grid at specified coordinates.
    """
    # Convert grid coordinates to pixel coordinates
    x = x * box_size + box_size
    y = y * box_size + box_size
    
    board.create_line(x, y, x, y + box_size, fill='red', width=12)
    return board