# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from vidgear.gears import ScreenGear
import cv2

# open any valid video stream(for e.g `test.mp4` file)
# stream = VideoGear(source='test.mp4').start()

stream = ScreenGear(monitor=2).start()

# activate jpeg encoding and specify other related parameters
options = {'compression_format': '.jpg', 'compression_param':[cv2.IMWRITE_JPEG_QUALITY, 50]}

#Define NetGear Server with defined parameters
server = NetGear(pattern = 1, logging = True, **options)

# loop over until KeyBoard Interrupted
while True:

  try:

     # read frames from stream
    frame = stream.read()

    # check for frame if None-type
    if frame is None:
        break

    # {do something with the frame here}

    # send frame to server
    server.send(frame)

  except KeyboardInterrupt:
    break

# safely close video stream
stream.stop()

# safely close server
server.close()