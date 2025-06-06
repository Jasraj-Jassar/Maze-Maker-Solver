import tkinter as tk
from grid import make_grid
from remove_line import clear_grid_line
from standardize import standardize_start_end

# Initialize main window
window = tk.Tk()

# Define grid dimensions
box_size = 160  # Size of each grid cell
margin = 160    # Margin around the grid

maze = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,1,0,1],
    [1,0,1,0,1],
    [1,1,1,1,1]
]

# Create the grid and standardize start/end positions
board = make_grid(maze, box_size, window)
standard_start_end = standardize_start_end(box_size, margin, board)
# Start the main event loop
window.mainloop() 