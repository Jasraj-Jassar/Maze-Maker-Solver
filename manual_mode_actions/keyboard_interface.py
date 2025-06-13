import tkinter as tk

def keyboard_interface(event):
    """
    Handles arrow key inputs and returns corresponding row and column changes.

    """
    row_change = 0
    col_change = 0
    
    if event.keysym == 'Up':
        col_change = -1
    elif event.keysym == 'Down':
        col_change = 1
    elif event.keysym == 'Left':
        row_change = -1
    elif event.keysym == 'Right':
        row_change = 1
        
    return row_change, col_change