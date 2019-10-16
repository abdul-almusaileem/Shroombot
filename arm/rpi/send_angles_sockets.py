
import socket
import struct

# this method is going to take an array of angles, host ip and port number
# it then initiate a socket connection with the esp over the specified (ip,port) 
# then sends the angles via that socket
#
def send_angles(ip, port=5001, angles=[]):
    
    # initiate the socket
    #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        # connect to the specified ip and port
        #
        sock.connect((ip, port))
        
        # declare connection
        #
        print("connected to: {}".format(ip))
        
        # convert each angle value from float to byte then send it
        #
        for angle in angles:
            angle_data = struct.pack("f", angle)
            sock.send(angle_data)
    