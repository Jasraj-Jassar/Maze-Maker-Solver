def goal_setter(x, y, box_size, margin, board):
    """
    Removes a vertical line from the grid at specified coordinates.
    """
    # Convert grid coordinates to pixel coordinates
    x = x * box_size + box_size
    y = y * box_size + box_size
    
    board.create_rectangle(x, y, x - box_size, y + box_size, fill='green')
    return board