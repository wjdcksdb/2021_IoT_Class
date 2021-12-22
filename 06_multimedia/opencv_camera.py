# import cv2

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Camera open fail")
#     exit()

# ret, frame = cap.read()
# cv2.imwrite('output.jpg',frame)
# cap.release()
# cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open fail")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()