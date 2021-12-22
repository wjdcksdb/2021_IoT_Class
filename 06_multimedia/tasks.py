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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge3 = cv2.Canny(frame,150,200)
    cv2.imshow('edge',edge3)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(10) == 13:
        break

out.release()
cv2.destroyAllWindows()