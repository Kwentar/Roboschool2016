import pyupm_i2clcd as lcd
import cv2

display = lcd.Jhd1313m1(0, 0x3E, 0x62)
cap = cv2.VideoCapture()
cap.open(0)
cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')
for _ in range(100):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray) 
        display.clear()
        display.write("founded {} faces".format(len(faces)))
