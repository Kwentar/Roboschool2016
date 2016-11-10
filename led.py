import mraa 
import time 
led = mraa.Gpio(13)
led.dir(mraa.DIR_OUT) 
for _ in range(10):
    led.write(1)  # turn on
    time.sleep(1)  # wait 1 sec
    led.write(0)  # turn off
    time.sleep(1)  # wait 1 sec
