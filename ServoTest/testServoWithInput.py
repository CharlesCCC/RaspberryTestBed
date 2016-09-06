import RPi.GPIO as gpio
import time

outpin = 40
gpio.setmode(gpio.BOARD)
gpio.setup(outpin,gpio.OUT)
p = gpio.PWM(outpin,50)
p.start(7.5)

while True:
	try:
		position=input("Where do you want to go 0-180 degree?")
		DC=1./20.*(position)+2.5
		p.ChangeDutyCycle(DC)
	except KeyboardInterrupt:
		p.stop()
		gpio.cleanup()
		exit()
