# # import required libraries
# from vidgear.gears import VideoGear
# from vidgear.gears import NetGear
# from vidgear.gears import ScreenGear
# import cv2
#
# # open any valid video stream(for e.g `test.mp4` file)
# # stream = VideoGear(source='test.mp4').start()
#
# stream = ScreenGear(monitor=1).start()
#
# # activate jpeg encoding and specify other related parameters
# options = {'compression_format': '.jpg', 'compression_param':[cv2.IMWRITE_JPEG_QUALITY, 50]}
#
# #Define NetGear Server with defined parameters
# # server = NetGear(pattern = 1, logging = True, **options)
#
#
# # Define Netgear Client at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with yours !!!)
# # server = NetGear(address = '192.168.88.248', port = '48000', protocol = 'udp',  pattern = 1, logging = True, **options)
# server = NetGear(address = '192.168.88.221', port = '48000', protocol = 'udp',  pattern = 1, logging = True, **options)

# import libraries
from vidgear.gears.asyncio import NetGear_Async
from vidgear.gears import ScreenGear
import asyncio

# stream = ScreenGear(monitor=1).start()

#initialize Server with suitable source and enable stabilization
# server=NetGear_Async( address='192.168.88.221', port = '48000', protocol = 'udp', pattern=2, logging=True)

from vidgear.gears.asyncio import NetGear_Async
import cv2, asyncio

# import libraries
from vidgear.gears.asyncio import NetGear_Async
import asyncio

#initialize Server with suitable source and enable stabilization
stream = ScreenGear(monitor=1).start()
server=NetGear_Async(source=stream, stabilize=True, logging=True).launch()

if __name__ == '__main__':
    #set event loop
    asyncio.set_event_loop(server.loop)
    try:
        #run your main function task until it is complete
        server.loop.run_until_complete(server.task)
    except (KeyboardInterrupt, SystemExit):
        #wait for interrupts
        pass
    finally:
        # finally close the server
        server.close()