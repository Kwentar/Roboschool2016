import cv2
import mraa
import subprocess

btn = mraa.Gpio(3)
btn.dir(mraa.DIR_IN)
cap = cv2.VideoCapture()
cap.open(0)
btn_down = False
for _ in range(100):
    btn_state = btn.read()
    if not btn_state and btn_down:
        btn_down = False
    if btn_state and not btn_down:
        print("down")
        cv2.imwrite("test.png", frame)
        output = subprocess.check_output("./darknet classifier predict cfg/imagenet1k.dataset cfg/darknet.cfg darknet.weights /home/root/test.png", cwd="/home/root/darknet/", shell=True )
        out_split = output.split('\n')
        t = out_split[1].split(':')[1].split()[2]
        class_ = out_split[2].split(':')[0]
        print("{} sec, class is: ".format(t, class_))
        btn_down = True
    ret, frame = cap.read()
