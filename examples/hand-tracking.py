import cv2
import pycamdetector as pcam

pTime = 0
cap = cv2.VideoCapture(0)
detector = pcam.HandDetector(detectionCon=0.85, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    if len(lmList) != 0:
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        print(totalFingers)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
