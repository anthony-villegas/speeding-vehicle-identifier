# source https://pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

import cv2
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

def frame_capture(self, frame_capture_action):
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame_capture_action.schedule(0, frame.array)
        rawCapture.truncate(0)
        
