import cv2
import numpy as np

#Resourse: https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html

def mouse_pos_opencv(canvas_img):
    # Convert the image to grayscale
    canvas_mouse_pos = canvas_img

    #Filtering the other colors so only red mouse is visible
    canvas_hsv_img = cv2.cvtColor(canvas_img, cv2.COLOR_BGR2HSV)
    canvas_mask_img = cv2.inRange(canvas_hsv_img, (0, 100, 100), (10, 255, 255))

    canvas_gray_img = cv2.cvtColor(canvas_img, cv2.COLOR_BGR2GRAY) # TODO: for future use, if needed

    rows = canvas_gray_img.shape[0]
    
    circles_pos = cv2.HoughCircles(
        canvas_mask_img,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=30,
        param1=100,
        param2=15,           # Lower for higher sensitivity as we can only see red mouse in canvas_mask_img
        minRadius=15,
        maxRadius=70
    )
    
    if circles_pos is not None:
        print("Circles found:", circles_pos)
        circles_pos = np.uint16(np.around(circles_pos))
        for i in circles_pos[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(canvas_mouse_pos, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(canvas_mouse_pos, center, radius, (0, 120, 0), 3)
    
    return canvas_mouse_pos, circles_pos