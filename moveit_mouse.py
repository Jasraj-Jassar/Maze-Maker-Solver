import tkinter as tk
def red_mouse(row, col, margin, box_size, board, color):
    """
    Creates a user interface for the maze game.
    """

    if row >= -1 or col >= -1:
        x1 = row * box_size + margin
        y1 = col * box_size + margin
        x2 = x1 + box_size
        y2 = y1 + box_size
        board.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    return board