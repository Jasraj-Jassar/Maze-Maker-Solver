import cv2
import random


#Random maze solver it will use random moves to find a path from the start till the end of the maze.
def random_solver(canvas_mouse_pos, circles_pos):

    # check if the top of the mouse is movable path
    circle_pos_x = int(circles_pos[0][0][0])  # x
    circle_pos_y = int(circles_pos[0][0][1])  # y
   
    directions = {
        "Down": (circle_pos_y + 60, circle_pos_x),
        "Up": (circle_pos_y - 60, circle_pos_x),
        "Left": (circle_pos_y, circle_pos_x - 60),
        "Right": (circle_pos_y, circle_pos_x + 60),
    }

    valid_moves = []

    for direction, (cy, cx) in directions.items():
        if 0 <= cy < canvas_mouse_pos.shape[0] and 0 <= cx < canvas_mouse_pos.shape[1]:
            b, g, r = canvas_mouse_pos[cy, cx]
            if b < 200 and g < 200 and r < 200:
                print(f"Movable path {direction.lower()}")
                valid_moves.append(direction)

    return random.choice(valid_moves) if valid_moves else None