from utils.keyboard_interface import keyboard_interface
from parameters import row, col
from grid_gen_and_utils.Initialize import maze_board
from utils.updatePos import update_position

def manual_mode(event):

    print("Manual mode enabled")

    update_position(event)
