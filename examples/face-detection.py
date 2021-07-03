import cv2
import pycamdetector
import time

cap = cv2.VideoCapture(0)
pTime = 0
detector = pycamdetector.FaceDetector(minDetectionCon=0.7)
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    print(bboxs)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow('Pycamdetector', img)
    cv2.waitKey(1)
