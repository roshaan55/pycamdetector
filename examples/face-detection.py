import cv2
import pycamdetector
import time

cap = cv2.VideoCapture(0)
pTime = 0
detector = FaceDetector(minDetectionCon=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, showPercentage=False)
    print(bboxs)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv2.imshow('MediaPipe Face Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
