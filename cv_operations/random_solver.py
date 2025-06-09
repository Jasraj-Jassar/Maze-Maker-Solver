import cv2
import random


#Random maze solver it will use random moves to find a path from the start till the end of the maze.
def random_solver(canvas_mouse_pos, circles_pos):

    # check if the top of the mouse is movable path
    circle_pos_x = int(circles_pos[0][0][0])  # x
    circle_pos_y = int(circles_pos[0][0][1])  # y
    circle_radius = int(circles_pos[0][0][2]) # radius

    check_below = circle_pos_y + 60
    check_above = circle_pos_y - 60
    check_left = circle_pos_x - 60
    check_right = circle_pos_x + 60

    while True:
        cases = [0, 1, 2, 3]
        random.shuffle(cases)

        for case_num in cases:
            match case_num:
                case 0:  # Down
                    if 0 <= check_below < canvas_mouse_pos.shape[0]:
                        b, g, r = canvas_mouse_pos[check_below, circle_pos_x]
                        if b < 200 and g < 200 and r < 200:
                            print("Movable path below")
                            return "Down"
                        else:
                            break  # restart

                case 1:  # Up
                    if 0 <= check_above < canvas_mouse_pos.shape[0]:
                        b, g, r = canvas_mouse_pos[check_above, circle_pos_x]
                        if b < 200 and g < 200 and r < 200:
                            print("Movable path above")
                            return "Up"
                        else:
                            break

                case 2:  # Left
                    if 0 <= check_left < canvas_mouse_pos.shape[1]:
                        b, g, r = canvas_mouse_pos[circle_pos_y, check_left]
                        if b < 200 and g < 200 and r < 200:
                            print("Movable path left")
                            return "Left"
                        else:
                            break

                case 3:  # Right
                    if 0 <= check_right < canvas_mouse_pos.shape[1]:
                        b, g, r = canvas_mouse_pos[circle_pos_y, check_right]
                        if b < 200 and g < 200 and r < 200:
                            print("Movable path right")
                            return "Right"
                        else:
                            break
        # If no valid direction found in this loop, it will retry with a fresh shuffle
