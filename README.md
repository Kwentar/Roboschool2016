## Работа с Intel Edison
### Установка OpenCV:

Добавляем пакеты в файл /etc/opkg/base-feeds.conf:

src all http://iotdk.intel.com/repos/2.0/iotdk/all

src x86 http://iotdk.intel.com/repos/2.0/iotdk/x86

src i586 http://iotdk.intel.com/repos/2.0/iotdk/i586

Затем запускаем:
```
opkg update
opkg install python-numpy opencv python-opencv
```
### Проверка OpenCV:

* Запускаем Python
* Выполняем:
```python
import cv2
print(cv2.__version__)
```
Если видим "2.4.9" или что-то вроде того, то все хорошо

### Проверка работоспособности камеры:

`lsmod | grep uvc`, если вывод не пустой - скорее всего все работает, если пустой - попробовать `opkg install kernel-module-uvcvideo`

В коде:
```python
>>> import cv2
>>> cap = cv2.VideoCapture()
>>> cap.open(0)
True
>>> ret, frame = cap.read()
>>> ret
True
>>> frame.shape
(480, 640, 3)
```

### Установка Darknet:

```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```
### Проверка Darknet
`./darknet`

Правильный вывод: `usage: ./darknet <function>`

### Работа с перефирией: 
пакет для работы с вводом-выводом - `mraa`

#### Помигать диодиком:
```python
import mraa
import time
led = mraa.Gpio(2)
led.dir(mraa.DIR_OUT)
for _ in range(10):
    led.write(1)  # turn on
    time.sleep(1)  # wait 1 sec
    led.write(0)  # turn off
    time.sleep(1)  # wait 1 sec
```
#### Работа с кнопкой:
```python
import mraa
btn = mraa.Gpio(3)
btn.dir(mraa.DIR_IN)
btn_down = False
btn_state = btn.read()
# cycle:
    if not btn_state and btn_down:
        btn_down = False
    if btn_state and not btn_down:
        print("down")
        # do all stuff here
        btn_down = True
```


#### Работа с экраном:
подключение:
```python
import pyupm_i2clcd as lcd
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
```
выводим текст:
```python
display.write("Roboschool")
```
очищаем:
```python
display.clear()
```
управляем курсором:
```python
display.setCursor(0,0)  # строка, столбец
```
меняем цвет подсветки:
```python
display.setColor(r, g, b)
```

