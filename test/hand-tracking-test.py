import cv2
import pycamdetector as pcam

cap = cv2.VideoCapture(0)
# FPSReader = pcam.FPS()  # Method to show FPS.
detector = pcam.HandDetector(detectionCon=0.85, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img, flipType=False)  # with draw
    hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

        # if len(hands) == 2:
        #     # Hand 2
        #     hand2 = hands[1]
        #     lmList2 = hand2["lmList"]  # List of 21 Landmark points
        #     bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
        #     centerPoint2 = hand2['center']  # center of the hand cx,cy
        #     handType2 = hand2["type"]  # Hand Type "Left" or "Right"
        #
        #     fingers2 = detector.fingersUp(hand2)
        #
        #     # Find Distance between two Landmarks. Could be same hand or different hands
        #     length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
        #     # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw

    # Display
    fps, img = FPSReader.showFPS(img)  # display fps on screen
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
