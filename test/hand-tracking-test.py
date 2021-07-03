import cv2
import time
import pycamdetector

pTime = 0
cap = cv2.VideoCapture(0)
detector = pycamdetector.handDetector(detectionCon=0.85, maxHands=1)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        print(totalFingers)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
