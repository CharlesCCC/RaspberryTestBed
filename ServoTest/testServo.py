import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(22,gpio.OUT)
p = gpio.PWM(22,50)
p.start(7.5)

while True:
	try:
		p.ChangeDutyCycle(2.5)
		time.sleep(1)
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
	except KeyboardInterrupt:
		p.stop()
		gpio.cleanup()
		exit()
