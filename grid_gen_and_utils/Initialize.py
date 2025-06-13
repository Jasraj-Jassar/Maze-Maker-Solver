import tkinter as tk
from parameters import row, col, box_size, margine
from grid_gen_and_utils.make_grid import make_grid
from grid_gen_and_utils.random_grid import random_grid_genrator
from grid_gen_and_utils.standardize_start_end import standardize_start_end
from grid_gen_and_utils.red_mouse import red_mouse

class MazeBoard:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MazeBoard, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        # Initialize main window
        self.window = tk.Tk()
        
        # Create maze and board
        self.maze = random_grid_genrator(row, col)
        self.board = make_grid(self.maze, margine, box_size, self.window)
        self.standard_start_end = standardize_start_end(margine, box_size, self.board, row, col)
        
        #Initialize position
        self.board, self.current_row, self.current_col = red_mouse(margine, box_size, self.board)
    
    def get_board(self):
        return self.board
    
    def get_window(self):
        return self.window
    
    def get_position(self):
        return self.current_row, self.current_col
    
    def update_position(self, new_row, new_col):
        self.current_row = new_row
        self.current_col = new_col
        red_mouse(margine, box_size, self.board, "red", self.current_row, self.current_col)
        return self.current_row, self.current_col
    
    def clear_board(self):
        """Clear the red dot from the current position"""
        # Clear the current position
        red_mouse(margine, box_size, self.board, "black", self.current_row, self.current_col)
        # Update the board
        self.board.update()

# Create a singleton instance
maze_board = MazeBoard()
