# pycamdetector
Python package to detect face landmarks(468), detect face, pose estimations, object detection, and least but not last track the hands and also detect its landmarks(21) by using Webcam.

Major bugs and fixes are resolved in **pycamdetector 0.5.1**. It is a reviesd update of previous version **pycamdetector 0.5** which icludes some additional new fuctions such as imagesStack, cornerRect, putRectText and all the necessary functions used for Computer Vision using OpenCV using

## Installation:
```nano
pip install pycamdetector
```
## For Upgradation(pycamdetector):
```nano
pip install --upgrade pycamdetector
```

## Basic Code to open Webcam:
```py
import cv2

cap = cv2.VideoCapture(0)
while True:
    # Get image frame
    success, img = cap.read()
    # Display or open webcam
    cv2.imshow("Image", img)
    # press q to close or terminate the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

## Additional Functions:
* ImagesStack
* cornerRect
* findContours
* PNGOverlay
* imageRotate
* putRectText

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

## Face Detection Usage:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, showPercentage=False)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
The above funtion **findFaces()** takes three optional parameters from user: **drawRect**, **showPercentage**, and **textColor**
### 1. drawRect:
Its a boolean value which takes the input as **true** or **false**, is used to draw the rectangle around the faces detected by a BGR Image or webcam input.
By default it is true and draws the rectangle around the faces. If you don't want to draw rectangle around the faces detected, follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, drawRect=False)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 2. showPercentage:
Its a boolean value which takes the input as **true** or **false**, is used to display the accuracy percentage of the faces detected by a BGR Image or webcam input.
By default it is true and displays the accuracy percentage of the faces detected. If you don't want to display percentage, follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, showPercentage=False)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 3. textColor:
It is a color of text used to display accuracy percentage.
By default the color of text is Purple(255, 0, 255). These are the BGR values and always accepts BGR(Blue, Green, Red) values. If you want to change the color simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetectionCon=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, textColor=(255,255,255))
    print(bboxs)
    cv2.imshow('Image', img)
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

## Images Stack usage
```py
import pycamdetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgList = [img, img, imgGray, img, imgGray, img,imgGray, img, img]
    stackedImg = pycamdetector.imagesStack(imgList, 3, 0.4)
    cv2.imshow("stacked Images", stackedImg)
    # press q to close or terminate the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

```

For more examples see [Examples](https://github.com/roshaan55/pycamdetector/blob/main/examples "Examples of funcions of pydetector").
