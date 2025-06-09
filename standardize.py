from remove_line import clear_grid_line

def standardize_start_end(row, col, margin, box_size, board):
    """
    Standardizes the start and end points of the grid.
    """

    # Define start point at top-left corner (0,0) Removed in order to not confuse the bot between start and end
    # start_x = 0
    # start_y = 0
    # clear_grid_line(start_x, start_y, box_size, margin, board)  

    end_x = row
    end_y = col - 1
    
    clear_grid_line(end_x, end_y, box_size, margin, board) 

    return board