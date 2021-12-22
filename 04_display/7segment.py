import RPi.GPIO as GPIO
import time
# GPIOI 7개 핀 번호 설정
#               A B C D E F G
# SEGMENT_PINS = [2,3,4,5,6,7,8]
SEGMENT_PINS = [22,27,3,2,17,10,9] 


GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

data = [1, 1, 1, 1, 1, 1, 0]

try:
    for _ in range(3):
        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i], data[i])

        time.sleep(1)

        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i], GPIO.LOW)
        
        time.sleep(1)
finally:
    GPIO.cleanup()
    print('bye')