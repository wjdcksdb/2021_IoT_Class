import RPi.GPIO as GPIO
import time

SERVO_PIN = 4
SWITCH_PIN = 8


GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
defau = 2.5
mode = 0
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5)
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        if val != 0:
            if mode == 0:
                pwm.ChangeDutyCycle(defau)
                if defau == 12.5:
                    mode = 1
                    continue
                defau += 5
            elif mode == 1:
                defau -= 5
                pwm.ChangeDutycycle()
                if defau == 2.5:
                    mode = 0 
        time.sleep(1)
finally:
    pwm.stop()
    GPIO.cleanup()



