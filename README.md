# pycamdetector
Python package to detect face landmarks(468), detect face, pose estimations, object detection, Multi-Hand Gesture Control and least but not last track the hands and also detect its landmarks(21) by using Webcam.

Major bugs and fixes are resolved in the new update **pycamdetector 0.5**

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

cap = cv2.VideoCapture(0)
detector = pcam.HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img, flipType=False)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
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
For more examples see [Examples](https://github.com/roshaan55/pycamdetector/blob/main/examples "Examples of funcions of pydetector").
