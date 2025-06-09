import cv2
import numpy as np

def goal_recognizer(canvas_img):
    # Convert the image to grayscale
    canvas_mouse_pos = canvas_img

    #Filtering the other colors so only red mouse is visible
    canvas_hsv_img = cv2.cvtColor(canvas_img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for green
    lower_green = np.array([35, 40, 40])  # Example values
    upper_green = np.array([85, 255, 255]) # Example values

    # Create a mask
    canvas_mask_img = cv2.inRange(canvas_hsv_img, lower_green, upper_green)

    # Detect edges
    edges = cv2.Canny(canvas_mask_img, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through contours and draw squares
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            cv2.drawContours(canvas_mouse_pos, [approx], 0, (0, 255, 0), 2)
            M = cv2.moments(approx)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                goal_box_coord = [cx, cy]
                return canvas_mouse_pos, goal_box_coord

