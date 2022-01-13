from pycamdetector.PlotModule import LivePlot
import cv2
import math

xPlot = LivePlot(width=1200, yLimit=[-100, 100], interval=0.01)
x = 0
while True:

    x += 1
    if x == 360:
        x = 0
    imgPlot = xPlot.update(int(math.sin(math.radians(x)) * 100))

    cv2.imshow("Image", imgPlot)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
