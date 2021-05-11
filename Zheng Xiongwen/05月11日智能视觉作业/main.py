'''
作品名称：走廊人体感应灯
实现功能：当光敏传感器检测到当前环境较黑的时，通过超声波判断是否有人进入走廊，当有人进入时LED灯点亮;
当环境特别黑且LED灯坏了的时候，蜂鸣器会响，警报经过的人可能有危险，也提醒检修人员进行修理;
居民也可通过触摸开关打开LED灯
'''
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import PCF8591 as ADC

#超声波
TRIG = 17 #GPIO0
ECHO = 18 #GPIO1
#LED灯
LED = 27 #GPIO2
#蜂鸣器
beep = 22 #GPIO3
#触摸开关
switch = 23 #GPIO4

flag = 0 #用于指示LED灯的状态(0为关，1为开)
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(LED, GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(beep, GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(switch, GPIO.IN)
    ADC.setup(0x48)

def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
    time2 = time.time()

    during = time2 - time1
    return during * 340 / 2 *100

def loop():
    global flag
    while True:
        guangqiang = ADC.read(0)
        dis = distance()
        if guangqiang > 180 and guangqiang < 200: #环境较黑
            GPIO.output(beep, GPIO.HIGH)
            if dis < 20: #有人进入
                GPIO.output(LED, GPIO.HIGH)
                flag = 1
            else:
                GPIO.output(LED, GPIO.LOW)
                flag = 0
        elif guangqiang > 200:
            GPIO.output(beep, GPIO.LOW)
        else:
            GPIO.output(beep, GPIO.HIGH)

        if GPIO.input(switch):
            if flag == 0:
                GPIO.output(LED, GPIO.HIGH)
                flag = 1
            else:
                GPIO.output(LED, GPIO.LOW)
                flag = 0

        print(dis, 'cm')
        print('')
        time.sleep(0.3)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()