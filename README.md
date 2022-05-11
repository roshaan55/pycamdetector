# pycamdetector
Python package to detect face landmarks(468), detect face, pose estimations, object detection, and least but not last track the hands and also detect its landmarks(21) by using Webcam.

The Previous version of pycamdetector **pycamdetector 0.5.4** was a reviesd update of previous version **pycamdetector 0.5** which included some additional new fuctions such as **imagesStack**, **cornerRect**, **putRectText** and all the necessary functions used for Computer Vision using **OpenCV Python**.

New Module **PlotModule** added in new update which is used to plot live graph.

In **pycamdetector 0.6** some new features are added in Face Detection Module which are: **rectColor**, **rectThick**, **corLen**, **corColor** and **corThick**.

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
If you have external webcam connected, then you have to pass **1** in **VideoCapture()** function.
### Code for External Webcam:
```py
import cv2

cap = cv2.VideoCapture(1)
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
* imgFlip
* ImagesStack
* cornerRect
* findContours
* PNGOverlay
* imageRotate
* putRectText

## Hand Detection Usage:
```py
import cv2
import pycamdetector as pcam

cap = cv2.VideoCapture(0)
detector = pcam.HandDetector(minDetConf=0.8, maxHands=2)
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
The **Hand Detection Module** contains three methods: **findHands()**, **fingersUp()** and **findDistance()**
The **findHands()** takes four optional parameters from user: **drawConns**, **flipType**, **bBox** and **showHandType**
### 1. drawConns:
Its a boolean value which takes the input as **true** or **false**, is used to draw the hand connections of hands detected in a BGR Image or by webcam input.
By default it is true and draws the hand connections.
If you don't want to draw the hand connectins on hand, you can pass draw as **False**.

**Note**: By default the drawConns takes two parameters: **hands** and **img** with **drawConns=True**. If you pass only **one parameter** with **drawConns=True** it will generate an error.

With **drawConns=True**
```py
hands, img = detector.findHands(img)
```
With **drawConns=False**
```py
hands = detector.findHands(img, drawConns=False)
```
### 2. flipType:
Its a boolean value which takes the input as **true** or **false**, is used to draw flip the type of hands detected in a BGR Image or by webcam input.
By default it is true and flips the hand type. If you don't want to flip the type of hand, you can pass flipType as **False**.

With **drawConns=True** and **flipType=False**
```py
hands, img = detector.findHands(img, fliptype=False)
```
With **drawConns=False** and **flipType=False**
```py
hands = detector.findHands(img, drawConns=False, fliptype=False)
```
### 3. bBox:
Its a boolean value which takes the input as **true** or **false**, is used to draw the bounding box around the hand detected in a BGR Image or by webcam input.
By default it is **false**. If you want to draw the bounding box around the hand detected, you can pass bBox as **True**.

With **drawConns=True** and **bBox=True**
```py
hands, img = detector.findHands(img, bBox=True)
```
With **drawConns=False** and **bBox=True**
```py
hands = detector.findHands(img, drawConns=False, bBox=True)
```
### 4. showHandType:
Its a boolean value which takes the input as **true** or **false**, is used to show the type of hand detected in a BGR Image or by webcam input.
By default it is **false**. If you want to show the hand type of hand detected, you can pass showHandType as **True**.

With **drawConns=True** and **showHandType=True**
```py
hands, img = detector.findHands(img, showHandype=True)
```
With **drawConns=False** and **showHandType=True**
```py
hands = detector.findHands(img, drawConns=False, showHandype=True)
```
The **fingersUp()** takes one parameter from user: **myHand**
The **findDistance()** takes two parameters from user: **p1** and **p2**

## Face Detection Usage:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, showPerc=False)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
In the **Face Detecion Module** the funtion of **findFaces()** takes three optional parameters from user: **drawRect**, **showPercentage**, and **textColor**.
New Features are added in new update of pycamdetector as mentioned above in the description.
In new update **pycamdetector 0.6** the parameter **showPercentage** changed to **showPerc**.
### 1. drawRect:
Its a boolean value which takes the input as **true** or **false**, is used to draw the rectangle around the faces detected in a BGR Image or by webcam input.
By default it is true and draws the rectangle around the faces. If you don't want to draw rectangle around the faces detected, follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, drawRect=False)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 2. showPerc:
Its a boolean value which takes the input as **true** or **false**, is used to display the accuracy percentage of the faces detected in a BGR Image or by webcam input.
By default it is true and displays the accuracy percentage of the faces detected. If you don't want to display percentage, follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, showPerc=False)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 3. textColor:
It is a color of text used to display accuracy percentage.
By default the color of text is White(255, 255, 255). These are the BGR values and always accepts BGR(Blue, Green, Red) values. If you want to change the color simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, textColor=(255,255,255))
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 4. rectColor:
It is a color of rectangle around the faces detected.
By default the color of rectangle is White(255, 255, 255). These are the BGR values and always accepts BGR(Blue, Green, Red) values. If you want to change the color simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, rectColor=(0, 255, 0))
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 5. rectThick:
It is the thickness of rectangle around the faces detected.
By default its thickness is 1. If you want to increase or decrease the thickness, simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, rectThick=2)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 6. corLen:
It is the length of corner lines of rectangle around the faces detected.
By default its length is 30. If you want to increase or decrease the length, simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, corLen=20)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 7. corColor:
It is the color of corner lines of rectangle around the faces detected.
By default the color of corners are Pink(255, 0, 255). These are the BGR values and always accepts BGR(Blue, Green, Red) values. If you want to change the color simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, corColor=(0, 0, 255))
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```
### 8. corThick:
It is the Thickness of the corners of rectangle around the faces detected.
By default the thickness of corners are 2. If you want to change the color simply follow the below code:
```py
import cv2
from pycamdetector.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector(minDetConf=0.85)
while True:
    success, img = cap.read()
    img = cv2.cv2.flip(img, 1)
    img, bboxs = detector.findFaces(img, corThick=3)
    print(bboxs)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

## FPS Usage
```py
import cv2
from FPS import FPS
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
```

## Images Stack usage
```py
import cv2
from FPS import FPS
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
