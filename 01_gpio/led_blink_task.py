import RPi.GPIO as GPIO
import time

LED_PIN  = [4, 17, 27]
GPIO.setmode(GPIO.BCM)
for x in LED_PIN:
    GPIO.setup(x, GPIO.OUT)

for x in LED_PIN:
    GPIO.output(x, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(x, GPIO.LOW)


GPIO.cleanup()
