from PIL import Image
import io
import numpy as np
import cv2

def capture_canvas(board):
    ps = board.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8'))).convert('RGB')  # <-- Fix is here
    opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return opencv_img
