def keyboard_interface(event):
    """
    Handles arrow key inputs and returns corresponding row and column changes.

    """
    
    moves = {
        'Up':    (0, -1),
        'Down':  (0,  1),
        'Left':  (-1, 0),
        'Right': (1,  0),
    }

    row_change, col_change = moves.get(event.keysym, (0, 0))
    return row_change, col_change
