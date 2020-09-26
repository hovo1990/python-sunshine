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

# import library
from vidgear.gears.asyncio import NetGear_Async
import cv2, asyncio

#initialize Server
server=NetGear_Async(address = '192.168.88.221', port = '48000', protocol = 'udp',  pattern = 1, logging = True,)

#Create a async frame generator as custom source
async def my_frame_generator():

        #Open any video stream such as live webcam video stream on first index(i.e. 0) device
        stream=ScreenGear(monitor=1).start()

        # loop over stream until its terminated
        while True:

            # read frames
            (grabbed, frame)= stream.read()

            # check if frame empty
            if not grabbed:
                #if True break the infinite loop
                break

            # do something with the frame to be sent here

            # yield frame
            yield frame
            # sleep for sometime
            await asyncio.sleep(0.00001)


if __name__ == '__main__':
    #set event loop
    asyncio.set_event_loop(server.loop)
    #Add your custom source generator to Server configuration
    server.config["generator"]=my_frame_generator()
    #Launch the Server
    server.launch()
    try:
        #run your main function task until it is complete
        server.loop.run_until_complete(server.task)
    except (KeyboardInterrupt, SystemExit):
        #wait for interrupts
        pass
    finally:
        # finally close the server
        server.close()