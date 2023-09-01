import cv2
import numpy as np

# Khởi tạo camera
cap = cv2.VideoCapture(0)

while True:
    # Đọc hình ảnh từ camera
    ret, img = cap.read()

    # Chuyển đổi sang không gian màu HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Xác định ngưỡng màu
    lower_color = np.array([0, 00, 50])
    upper_color = np.array([0, 00, 130])

    # Tạo mặt nạ
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Tìm đường viền
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Vẽ đường viền lên hình ảnh
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    # Tìm đường viền lớn nhất
    c = max(contours, key=cv2.contourArea)

    # Tính toán kích thước của vật thể
    x, y, w, h = cv2.boundingRect(c)
    focal_length = 500 # Tiêu cự của camera (mm)
    object_width = 150 # Chiều rộng thực tế của vật thể (mm)
    distance = (object_width * focal_length) / w

    # Hiển thị kết quả
    print(f'Distance: {distance} mm')

    # Hiển thị hình ảnh
    cv2.imshow('Image', img)
    
    # Kiểm tra phím thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
