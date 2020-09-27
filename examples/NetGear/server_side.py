# TODO WORKS
# import required libraries
from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from vidgear.gears.stabilizer import Stabilizer
from vidgear.gears import ScreenGear
import cv2

# open any valid video stream(for e.g `test.mp4` file)
# stream = VideoGear(source='test.mp4').start()

stream = ScreenGear(monitor=1).start()

# activate jpeg encoding and specify other related parameters
options = {'compression_format': '.jpg', 'compression_param':[cv2.IMWRITE_JPEG_QUALITY, 50]}

#Define NetGear Server with defined parameters
# server = NetGear(pattern = 1, logging = True, **options)


# Define Netgear Client at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with yours !!!)
# server = NetGear(address = '192.168.88.248', port = '48000', protocol = 'udp',  pattern = 1, logging = True, **options)
server = NetGear(address = '192.168.88.221', port = '48000', protocol = 'udp',  pattern = 1, logging = True, **options)
stab = Stabilizer()


# loop over until KeyBoard Interrupted
while True:

  try:

     # read frames from stream
    frame = stream.read()

    # check for frame if None-type
    if frame is None:
        break

    # {do something with the frame here}
    # send current frame to stabilizer for processing
    stabilized_frame = stab.stabilize(frame)

    # wait for stabilizer which still be initializing
    if stabilized_frame is None:
         continue

         # send frame to server
    # server.send(frame)
    server.send(stabilized_frame)

  except KeyboardInterrupt:
    break

# safely close video stream
stream.stop()

# safely close server
server.close()