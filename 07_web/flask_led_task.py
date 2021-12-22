from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN = 4
LED_PIN2 = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href="/led/on">RED LED ON</a>
    <a href="/led/off">RED LED OFF</a>
    <br>
    <a href="/led/on2">BLUE LED ON</a>
    <a href="/led/off2">BLUE LED OFF</a>
    
    '''

@app.route("/<color>/<op>")
def led_op(color,op):
    if op == "on":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.HIGH)
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.HIGH)
        
        return '''
        <p>LED ON</p>
        <a href="/">Go Home</a>
        '''
    elif op == "off":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.LOW)
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.LOW)
        return '''
        <p>LED OFF</p>
        <a href="/">Go Home</a>
        '''

   



if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()