import cv2

def img_processing(canvas_img):
    # Convert the image to grayscale
    canvas_gray_img = cv2.cvtColor(canvas_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Maze Capture", canvas_gray_img)
    cv2.waitKey(1)