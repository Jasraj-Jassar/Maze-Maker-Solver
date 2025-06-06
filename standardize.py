from remove_line import clear_grid_line

def standardize_start_end(box_size, margin, board):
    """
    Standardizes the start and end points of the grid.
    """
    # Define start point at top-left corner (0,0)
    start_x = 0
    start_y = 0

    end_x = 4
    end_y = 3

    # Remove the wall to create entrance and exit
    clear_grid_line(start_x, start_y, box_size, margin, board) 
    clear_grid_line(end_x, end_y, box_size, margin, board) 

    return board