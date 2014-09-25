import sys
import io
import time
from flask import Flask, Response, request

try:
  import picamera
except:
  # is there a better way to exit?
  sys.exit(0)

app = Flask(__name__)

if picamera:
  @app.errorhandler(picamera.PiCameraRuntimeError)
  def camera_is_in_use(e):
    return 'Error: camera is unavailable!', 503

@app.route('/smile', methods=['GET'])
def capture_photo():
  with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    # depending on how the camera is mounted use h/v flip:
    # camera.hflip = True
    # camera.vflip = True
    # is preview/sleep really needed ?
    camera.start_preview()
    time.sleep(0.1) # wait for camera to warm up
    stream = io.BytesIO()
    # capture a jpeg image as a stream of in-memory bytes:
    camera.capture(stream, format='jpeg', use_video_port=True)
    # rewind the stream:
    stream.seek(0)
  # send the stream(image) to a web browser (tested on Chrome/Safari):
  return Response(stream.read(), mimetype='image/jpeg')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
