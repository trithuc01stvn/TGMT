import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread('th.jpg', cv2.IMREAD_GRAYSCALE)

# Làm mịn ảnh
img = cv2.medianBlur(img, 5)

# Tìm cạnh
edges = cv2.Canny(img, 100, 200)

# Tìm đường viền
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ đường viền
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Phát hiện hình tròn
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # Vẽ đường tròn
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.putText(img, "circle", (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # Vẽ tâm
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)



# Xác định hình dạng của vật thể
for cnt in contours:
    # Xác định số lượng cạnh
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
    num_edges = len(approx)
    
    # Tính chu vi và diện tích
    perimeter = cv2.arcLength(cnt, True)
    area = cv2.contourArea(cnt)
    

    # Xác định hình dạng
    if num_edges == 3:
        shape = 'Triangle'
    elif num_edges == 4:
        shape = 'Square'
    else:
        shape = ''
    
    # Vẽ hình dạng lên ảnh
    M = cv2.moments(cnt)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)

    


# Hiển thị kết quả
cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
