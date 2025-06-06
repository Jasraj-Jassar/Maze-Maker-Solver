import tkinter as tk

def make_grid(box_size, window):
    """
    Creates a 4x4 grid of boxes on the given window.
    """
    window.configure(bg='black')
    
    board = tk.Canvas(window, 
                     width=box_size*4 + box_size*2, 
                     height=box_size*4 + box_size*2,
                     bg='black', 
                     highlightthickness=0)
    board.pack()

    for row in range(4):
        for col in range(4):
            start_x = col * box_size + box_size  # margin = box_size
            start_y = row * box_size + box_size
            end_x = start_x + box_size
            end_y = start_y + box_size

            board.create_rectangle(start_x, start_y, end_x, end_y,
                                 fill='black',
                                 outline='white')

    return board
