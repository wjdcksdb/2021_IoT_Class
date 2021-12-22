import RPi.GPIO as GPIO

LED_PIN = 2
SWITCH_PIN = 12

LED_PIN2 = 4
SWITCH_PIN2 = 10

LED_PIN3 = 20
SWITCH_PIN3 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        print(val)
        GPIO.output(LED_PIN, val)
        
        val = GPIO.input(SWITCH_PIN2)
        print(val)
        GPIO.output(LED_PIN2, val)

        val = GPIO.input(SWITCH_PIN3)
        print(val)
        GPIO.output(LED_PIN3, val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
