#!/usr/bin/env python
import RPi.GPIO as GPIO
import PCF8591 as ADC
import time

TiltPin = 11
Gpin   = 12
Rpin   = 13
DO = 15
Buzzer = 16

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
	GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(TiltPin, GPIO.BOTH, callback=detect, bouncetime=200)
	ADC.setup(0x48)
	GPIO.setup(DO, GPIO.IN)

def setup(pin):
	global BuzzerPin
	BuzzerPin = pin
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BuzzerPin, GPIO.OUT)
	GPIO.output(BuzzerPin, GPIO.HIGH)

def on():
	GPIO.output(BuzzerPin, GPIO.LOW)

def off():
	GPIO.output(BuzzerPin, GPIO.HIGH)

def beep(x):
	on()
	time.sleep(x)
	off()
	time.sleep(x)

def Led(x):
	if x == 0:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 1:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)

def Print(x):
	if x == 0:
		print '    *************'
		print '    *   Tilt!   *'
		print '    *************'

def detect(chn):
	Led(GPIO.input(TiltPin))
	Print(GPIO.input(TiltPin))

def loop():
    	status = 1
	while True:
		print 'SHINEValue: ', ADC.read(0)
				beep(0.5)
		time.sleep(0.2)

def destroy():
	GPIO.output(Gpin, GPIO.HIGH)       # Green led off
	GPIO.output(Rpin, GPIO.HIGH)       # Red led off	
	GPIO.output(BuzzerPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

