import cv2
import pycamdetector

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

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
