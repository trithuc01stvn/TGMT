import cv2

ip = "192.168.1.121"
port = "4747"

# Khởi tạo đối tượng VideoCapture
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(f'http://{ip}:{port}/video')

# Kiểm tra xem camera có hoạt động không
if not cap.isOpened():
    raise Exception("Không thể mở camera")

# Lặp vô hạn để hiển thị hình ảnh từ camera
while True:
    # Đọc hình ảnh từ camera
    ret, frame = cap.read()

    # Nếu không đọc được hình ảnh thì thoát khỏi vòng lặp
    if not ret:
        break

    # Hiển thị hình ảnh
    cv2.imshow('frame', frame)

    # Nếu nhấn phím 'q' thì thoát khỏi vòng lặp
    if cv2.waitKey(1) == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
