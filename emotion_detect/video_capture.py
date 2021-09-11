import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/cmaster/Desktop/emotion-detect/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('C:/Users/cmaster/Desktop/emotion-detect/video1.mp4')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()


