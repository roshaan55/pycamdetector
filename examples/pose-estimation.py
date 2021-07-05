import cv2
import time
import pycamdetector

cap = cv2.VideoCapture(0)
detector = pycamdetector.poseDetector()
pTime = 0
while True:
    success, img = cap.read()
    img = detector.findPose(img, draw=False)
    # img = cv2.flip(img, 1)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
