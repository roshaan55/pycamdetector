import cv2
from pycamdetector.FPS import FPS
# import time # import time module when you don't want webcam

# """
# Without Webcam
# """
# fpsReader = FPS()
# while True:
#     time.sleep(0.025)  # add delay to get 40 Frames per second
#     fps = fpsReader.showFPS()
#     print(fps)

"""
With Webcam
"""
FPSReader = FPS()
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    fps, img = FPSReader.showFPS(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
