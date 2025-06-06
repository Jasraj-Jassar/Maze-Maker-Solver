import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

def make_grid(box_size, window):
    margin = 160
    board = tk.Canvas(window, width=box_size*4 + margin*2, height=box_size*4 + margin*2,bg='black', highlightthickness=0)
    board.pack()

    # Draw boxes
    for row in range(4):
        for col in range(4):
            start_x = col * box_size + margin
            start_y = row * box_size + margin
            end_x = start_x + box_size
            end_y = start_y + box_size

            board.create_rectangle(start_x, start_y, end_x, end_y,
                                   fill='black',
                                   outline='white')

    return board
