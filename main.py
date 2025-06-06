import tkinter as tk
from grid import make_grid
from remove_line import clear_grid_line
from standardize import standardize_start_end
from random_grid import random_grid_genrator

# Initialize main window
window = tk.Tk()

# Define grid dimensions
row = 8  # Number of rows
col = row  # Number of columns, assuming a square grid
box_size = 160  # Size of each grid cell
margine = box_size


maze = random_grid_genrator(row, col)
# Create the grid and standardize start/end positions
board = make_grid(maze, margine, box_size, window)
standard_start_end = standardize_start_end(row, col, margine, box_size, board)
# Start the main event loop
window.mainloop() 