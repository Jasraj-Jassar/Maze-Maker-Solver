from grid_gen_and_utils.goal_setter import goal_setter

def standardize_start_end(margin, box_size, board, row = 0, col = 0):
    """
    Standardizes the start and end points of the grid.
    """

    # Define start point at top-left corner (0,0) Removed in order to not confuse the bot between start and end
    # start_x = 0
    # start_y = 0
    # goal_setter(start_x, start_y, box_size, margin, board)  

    end_x = row
    end_y = col - 1
    
    goal_setter(end_x, end_y, box_size, margin, board) 

    return board