import cv2
import numpy as np


cap = cv2.VideoCapture(1)

# Tiêu cự của camera (mm)
focal_length = 700

# Khoảng cách từ camera tới đối tượng (mm)
distance = 600

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_black = np.array([0, 50, 50])
    upper_black = np.array([10, 255, 155])
    
    mask = cv2.inRange(hsv, lower_black, upper_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Tính diện tích thực của vật thể
        area = ((cv2.contourArea(contour) * distance) / focal_length) / 100
        cv2.putText(frame, f"{area : .0f} c", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(area)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
