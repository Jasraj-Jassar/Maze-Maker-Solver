from grid_gen_and_utils.keyboard_interface import keyboard_interface
from parameters import row, col
from grid_gen_and_utils.Initialize import maze_board

def update_position(event):

    #Takes in an event from keyboard_interface and updates the position on the maze_board using maze_board methods

    current_row, current_col = maze_board.get_position()
    new_row, new_col = keyboard_interface(event)

    new_row = max(0, min(current_row + new_row, row - 1))
    new_col = max(0, min(current_col + new_col, col - 1))

    if (current_row, current_col) == (new_row, new_col):
        print("Invalid Move")
        return

    maze_board.clear_board()
    maze_board.update_position(new_row, new_col)
    print(f"Current Position: ({new_row}, {new_col})")

    if new_row == row - 1 and new_col == col - 1:
        print("Reached the end of the maze!")
        maze_board.get_window().quit()