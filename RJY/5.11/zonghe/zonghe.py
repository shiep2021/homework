import RPi.GPIO as GPIO
import time

TRIG = 11
ECHO = 12
trig=32

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(38,GPIO.OUT)
    GPIO.setup(36, GPIO.IN)
    GPIO.setup(trig,GPIO.OUT,initial=GPIO.HIGH)
def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    
    while GPIO.input(ECHO) == 0:
            a = 0
    time1 = time.time()
    while GPIO.input(ECHO) == 1:
            a = 1
    time2 = time.time()
    
    during = time2 - time1
    return during * 340/2*100

def loop():
    while True:
        dis = distance()
        print(dis,'cm')
        print('')
        if GPIO.input(36):
            GPIO.output(trig,GPIO.LOW)
        else:
            GPIO.output(trig,GPIO.HIGH)   
        if dis <10:
            GPIO.output(38,GPIO.HIGH)            
            GPIO.output(16,GPIO.LOW)
            GPIO.output(18,GPIO.LOW)
        elif dis >10 and dis <30: 
            GPIO.output(18,GPIO.HIGH)
            GPIO.output(16,GPIO.LOW)
            GPIO.output(38,GPIO.LOW)
        else:
            GPIO.output(16,GPIO.HIGH)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(38,GPIO.LOW)
            time.sleep(0.3)

def destroy():
        GPIO.cleanup()
        
if __name__ == "__main__":
        setup()
        try:
                loop()
        except KeyboardInterrupt:
                destroy()
