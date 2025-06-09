import tkinter as tk

def red_mouse(row, col, margin, box_size, board, color):
    """
    Draws a circular marker (mouse) at the specified grid cell.
    """
    if row >= -1 or col >= -1:
        x1 = row * box_size + margin + 4
        y1 = col * box_size + margin + 4
        x2 = x1 + box_size - 8
        y2 = y1 + box_size - 8
        board.create_oval(x1, y1, x2, y2, fill=color, outline='black')

    return board
