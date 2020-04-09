import time
import picamera #Importing picamera module

with picamera.PiCamera() as camera: #The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks
    camera.start_preview()          # Starts the preview
    time.sleep(10)
    camera.stop_preview()           # Stops the preview


# Other commands
# camera.capture ('image'.jpg')                         Capturing image to a file
# camera.capture(my_stream, 'jpeg')                     Capturing to a stream
# camera.start_recording('my_video.h264')               Start Recording to a file
# camera.stop_recording()                               Stop Recording
# camera.start_recording(stream, quantization=23)       Recording to a stream

# Some properties
# camera.brightness = i                                 Adjusts the brightness of the camera (0<i<100)
# camera.resolution = (640, 480)                        Adjusts the resolution of camera
# camera.wait_recording(60)                             Records the video for given time

# For decoding the video:
# MP4Box -add pivideo.h264
# pivideo.mp4

#Documentation: https://picamera.readthedocs.io/en/release-1.13/