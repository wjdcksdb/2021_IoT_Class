import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()


try:
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(3)
    while True:
        a = input("photo:1, vidoe:2, exit:3 > ")
        if a == "1":
            print("사진 촬영")
            now_str = time.strftime("%Y%m%d_%H%M%s")
            camera.capture("%s/%s.jpg"% (path,now_str))
        elif a == "2":
            print("동영상 촬영")
            now_str = time.strftime("%Y%m%d_%H%M%s")
            camera.start_recording("%s/%s.h264" % (path,now_str))
            time.sleep(5)
            camera.stop_recording()
        elif a == "3":
            print("exit")
            break
        else :
            print("incorrect command")
    # camera.start_recording("%s/vide.h264" % path)
    # time.sleep(10)
    # camera.stop_recording()

finally:
    camera.stop_preview()
