import cv2


cap = cv2.VideoCapture()
cap.open(0)
cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')
for _ in range(100):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray) 
        print("founded {} faces".format(len(faces)))
