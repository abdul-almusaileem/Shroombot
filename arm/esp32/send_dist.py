
import socket
import struct
import sys
 
 # this method is to send the mushroom distance to the pi
#
def send_dist(z, addr="172.20.10.3", port=5002):
    # open a socket to connect 
    #
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    
    # connect to the given ip
    # 
    sock.connect((addr, port))
    
    # pack the value the send it via the socket
    #
    z_data = struct.pack("f", z)
    sock.send(z_data)
    sock.close()
    
    return 1
         