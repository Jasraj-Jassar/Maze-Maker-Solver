import tkinter as tk
from grid import make_grid
from grid import center_window
from start_end import clear_grid_line

# Make a window
window = tk.Tk()
window.configure(bg='black')

# How big should each box be?
box_size = 160

# Standardize starting and ending position for all the grids
x = 0
y = 0

# Create the grid
board = make_grid(box_size, window)
update_board = clear_grid_line(x ,y , box_size, board)
# Show the window
window.mainloop() 