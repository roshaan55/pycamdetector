# pycamdetector
Python package to detect face landmarks(468), detect face, pose estimations, object detection, Multi-Hand Gesture Control and least but not last track the hands and also detect its landmarks(21) by using Webcam.

Major bugs and fixes are resolved and Multi-Hand Gesture Control included in the new update **pycamdetector 0.4.4**

## Installation:
```nano
pip install pycamdetector
```
## For Upgradation(pycamdetector):
```nano
pip install --upgrade pycamdetector
```

## Usage:
```py
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
```

## Object Detection Usage:
```py
import cv2
import time
import pycamdetector

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


# Download these necessary files from this repository

configpath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightpath = 'frozen_inference_graph.pb'
labelsPath = 'coco.names'

detector = pycamdetector.ObjectDetector(weightpath, configpath, labelsPath)

while True:
    success, img = cap.read()
    img, indices = detector.DetectObject(img)
    print(indices)
    cv2.imshow("Output", img)
    cv2.waitKey(1)
```

## Multi-Hand Gesture Usage:
```py
import cv2
import pycamdetector as pcam

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = pcam.HandDetector(detectionCon=0.85, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findMultipleHands(img, drawBbox=True, flipType=False)  # with draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.MultiHandFingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.MultiHandFingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            # length, info, img = detector.findMultiHandDistance(lmList1[8], lmList2[8], img)  # with draw
            length, info, img = detector.findMultiHandDistance(centerPoint1,
                                                               centerPoint2, img)  # with no draw
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
```

For more examples see [Examples](https://github.com/roshaan55/pycamdetector/blob/main/examples "Examples of funcions of pydetector").
