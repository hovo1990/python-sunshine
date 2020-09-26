# import required libraries
from vidgear.gears import NetGear
import cv2


#define Netgear Client with `receive_mode = True` and default parameter
# client = NetGear(receive_mode = True)

# define various tweak flags
options = {'flag' : 0, 'copy' : False, 'track' : False,'smoothing_radius':100}
#
# # Define Netgear Client at given IP address and define parameters (!!! change following IP address '192.168.x.xxx' with yours !!!)
client = NetGear(address = '192.168.88.221', port = '48000', protocol = 'udp',  pattern = 1, receive_mode = True, logging = True, **options)


# loop over
while True:

    # receive frames from network
    frame = client.recv()

    # check for received frame if Nonetype
    if frame is None:
        break


    # {do something with the frame here}


    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()