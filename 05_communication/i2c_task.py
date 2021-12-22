from lcd import drivers
import datetime
import Adafruit_DHT


sensor = Adafruit_DHT.DHT11
DHT_PIN = 4
display = drivers.Lcd()


try:
    print('Writing to Display')
    display.lcd_display_string("Hello, World!!",1)
    while True:
        now = datetime.datetime.now()
        print(now.strftime("%x%X"))
        display.lcd_display_string(now.strftime("%x%X"),1)
        h, t = Adafruit_DHT.read_retry(sensor,DHT_PIN)
        if h is not None and t is not None:
            pass
        else:
            print('Read Error')
       
        display.lcd_display_string("%.1f*C, %.1f%%" % (t,h),2)
       

    
finally:
    print("cleaning up")
    display.lcd_clear()