import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    contours_red,_ = cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours_green,_ = cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow,_ = cv2.findContours(mask_yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours_red:
        area = cv2.contourArea(contour)
        if area > 500:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    for contour in contours_green:
        area = cv2.contourArea(contour)
        if area > 500:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    for contour in contours_yellow:
        area = cv2.contourArea(contour)
        if area > 500:
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
