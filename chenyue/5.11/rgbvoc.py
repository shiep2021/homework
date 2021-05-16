import time
import RPi.GPIO as GPIO
 
colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
R = 11
G = 12
B = 13
trigger_pin =15
echo_pin =16
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(trigger_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)
 
'''
TRIG 负责发射超声波，Echo 负责接收超声波
'''
def send_trigger_pulse():
    #发送超声波，一直发
    GPIO.output(trigger_pin,1)
    # 为了防止错误，因为紧接着就需要把发射端置为高电平
    time.sleep(0.0001)
    #发射端置为高电平
    GPIO.output(trigger_pin,0)
 
'''
ECHO 负责接收超声波
'''
def wait_for_echo(value,timeout):
    count = timeout
    #通过该代码持续获取ECHO的状态
    while GPIO.input(echo_pin)!= value and count>0:
        count = count-1
 
'''
计算距离
'''
def get_distance():
    # 发射
    send_trigger_pulse()
    # 接收高电平 1/True
    wait_for_echo(True,10000)
    # 等待
    start = time.time()
    #接收低电平
    wait_for_echo(False,10000)
    finish = time.time()
    pulse_len = finish-start
    distance_cm = pulse_len/0.000058
    if distance_cm >= 0 and distance_cm <= 20:
            GPIO.setup(R, GPIO.OUT)   
            GPIO.output(R, GPIO.HIGH) 
    elif distance_cm >= 21 and distance_cm <= 40:
            GPIO.setup(G, GPIO.OUT)   
            GPIO.output(G, GPIO.HIGH)  
    else:
            GPIO.setup(B, GPIO.OUT)   
            GPIO.output(B, GPIO.HIGH)  
    return distance_cm
 
while True:
    print("cm = %f"%get_distance())
    time.sleep(1)