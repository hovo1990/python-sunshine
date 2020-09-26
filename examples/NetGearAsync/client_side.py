# # import required libraries
# from vidgear.gears import NetGear
# import cv2
#
#
# #define Netgear Client with `receive_mode = True` and default parameter
# # client = NetGear(receive_mode = True)
#
# # define various tweak flags
# options = {'flag' : 0, 'copy' : False, 'track' : False,'smoothing_radius':100}
# #
# # # Define Netgear Client at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with yours !!!)
# client = NetGear(address = '192.168.88.221', port = '48000', protocol = 'udp',  pattern = 1, receive_mode = True, logging = True, **options)

# import libraries
from vidgear.gears.asyncio import NetGear_Async
import cv2, asyncio

#define and launch Client with `receive_mode=True`
client=NetGear_Async(address = '192.168.88.221', port = '48000', protocol = 'udp', receive_mode = True, logging = True).launch()


#Create a async function where you want to show/manipulate your received frames
async def main():
    # loop over Client's Asynchronous Frame Generator
    async for frame in client.recv_generator():


        # do something with received frames here


        # Show output window
        cv2.imshow("Output Frame", frame)
        key=cv2.waitKey(1) & 0xFF

        #await before continuing
        await asyncio.sleep(0.01)


if __name__ == '__main__':
    #Set event loop to client's
    asyncio.set_event_loop(client.loop)
    try:
        #run your main function task until it is complete
        client.loop.run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        #wait for interrupts
        pass

    # close all output window
    cv2.destroyAllWindows()
    # safely close client
    client.close()