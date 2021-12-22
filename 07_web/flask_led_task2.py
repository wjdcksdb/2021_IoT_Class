from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN = 4
LED_PIN2 = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/<color>/<op>")
def led_op(color,op):
    if op == "on":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return "RED LED ON"
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return "BLUE LED ON"
        
       
    elif op == "off":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.LOW)
            return "RED LED OFF"
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return "BLUE LED OFF"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()