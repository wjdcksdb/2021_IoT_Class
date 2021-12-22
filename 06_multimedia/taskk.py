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

import cv2

face_cascade = cv2.CascadeClassifier('./xml/face.xml')


if not cap.isOpened():
    print("Camera open fail")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()